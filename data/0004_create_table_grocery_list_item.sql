CREATE TABLE IF NOT EXISTS grocery.grocery_list_item (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  grocery_list_id BIGINT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT now(),
  modified_at TIMESTAMP
);