CREATE TABLE IF NOT EXISTS grocery.grocery_item (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT now(),
  modified_at TIMESTAMP,
  UNIQUE(name)
);