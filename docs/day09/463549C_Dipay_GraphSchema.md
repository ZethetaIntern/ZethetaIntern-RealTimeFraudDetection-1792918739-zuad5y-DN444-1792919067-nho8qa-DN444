# Property graph schema (Neo4j)

## Nodes

| Label | Properties |
|---|---|
| Card | card_hash, bin, issuer, product_type, created_at, fraud_flag |
| Account | account_id, type, status, opened_at |
| Customer | customer_hash, risk_tier |
| Device | device_fingerprint, os, browser, first_seen |
| IPAddress | ip_hash, country, city, is_vpn, is_proxy, is_tor |
| PhoneNumber | phone_hash, carrier, country |
| Email | email_hash, domain, disposable |
| PhysicalAddress | address_hash, city, state, country, zip |
| Merchant | merchant_id, mcc, name, risk_category |

## Edges

| Type | Properties |
|---|---|
| TRANSACTED_WITH | timestamp, amount, channel |
| SHARED_DEVICE | first_shared_at, last_shared_at |
| SHARED_ADDRESS | relationship_type |
| SAME_BENEFICIARY | transfer_count |
| LINKED_ACCOUNT | link_type |
| USED_IP | timestamp, session_duration |
| REGISTERED_PHONE | registration_date |
| REGISTERED_EMAIL | registration_date |

Indexes: `card_hash`, `device_fingerprint`, `ip_hash`; full-text on `Merchant.name`.

Louvain modularity **> 0.45** plus community size 8–500 flags a ring (too small = family; too large = popular merchant).
