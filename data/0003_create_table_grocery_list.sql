CREATE TABLE IF NOT EXISTS grocery.grocery_list (
  id BIGSERIAL PRIMARY KEY,
  completed TIMESTAMP,
  created_at TIMESTAMP NOT NULL DEFAULT now(),
  modified_at TIMESTAMP,
  UNIQUE(completed)
);