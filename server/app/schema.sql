CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password_hash TEXT NOT NULL,
    public_key TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS messages (
    message_id UUID PRIMARY KEY,
    sender_username TEXT NOT NULL REFERENCES users(username),
    recipient_username TEXT NOT NULL REFERENCES users(username),
    encryption_nonce TEXT NOT NULL,
    ciphertext TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL,
    delivered_at TIMESTAMPTZ,
    read_at TIMESTAMPTZ
);
