# Schema Registry configuration

- Product: Confluent Schema Registry (or Karapace).
- Subject strategy: `TopicNameStrategy` — `{topic}-value` and `{topic}-key`.
- Compatibility:
  - Default **BACKWARD** (consumers of new schema can read old data).
  - `audit.events-value`: **FULL** (no field drop; regulators replay years later).
- Evolution rules: add optional fields with defaults; never reuse field IDs; bump `schema_version` in payload.
- Auth: mTLS from producers; only `platform-streaming` CI role can register schemas.
- CI: Buf-like breaking change check on Avro in `api-specs/avro`.
