// 1 Community detection — Louvain communities with modularity proxy via dense shared devices
MATCH (d:Device)<-[:SHARED_DEVICE]-(c:Card)
WITH d, count(c) AS cards
WHERE cards >= 8
RETURN d.device_fingerprint AS hub, cards
ORDER BY cards DESC LIMIT 20;
// expected: devices used by many otherwise unrelated cards

// 2 PageRank-like degree on devices (GDS PageRank in prod)
MATCH (d:Device)
OPTIONAL MATCH (d)--(n)
RETURN d.device_fingerprint, count(n) AS degree
ORDER BY degree DESC LIMIT 10;

// 3 Shortest path to known fraud (2 hops risky, 6 hops weak)
MATCH (c:Card {card_hash: $card})
MATCH (f:Card {fraud_flag: true})
MATCH p = shortestPath((c)-[*..6]-(f))
RETURN length(p) AS hops, [n IN nodes(p) | labels(n)[0]] AS path;

// 4 Temporal growth — account farming
MATCH (c:Customer)-[r:REGISTERED_EMAIL|REGISTERED_PHONE|SHARED_DEVICE]-()
WHERE r.registration_date > datetime() - duration('P7D')
      OR r.first_shared_at > datetime() - duration('P7D')
WITH c, count(r) AS new_links
WHERE new_links > 10
RETURN c.customer_hash, new_links;

// 5 Triangulation template
MATCH (a:Card)-[:TRANSACTED_WITH]->(m:Merchant)
MATCH (m)<-[:TRANSACTED_WITH]-(b:Card)
MATCH (a)-[:SHARED_DEVICE]-(d:Device)<-[:SHARED_DEVICE]-(b)
WHERE a <> b
RETURN a.card_hash, b.card_hash, m.merchant_id, d.device_fingerprint
LIMIT 50;

// 6 Money-mule betweenness (bridge accounts)
MATCH (x:Account {type:'mule_suspect'})
MATCH (c1:Card)-[:LINKED_ACCOUNT]->(x)<-[:LINKED_ACCOUNT]-(c2:Card)
WHERE c1 <> c2
RETURN x.account_id, count(*) AS bridges
ORDER BY bridges DESC;

// Sample expected: hops=2 for shared-device with confirmed fraud card_hash=aaa → score boost
