# TradeVision AI - Database Design

## Tables

### stocks

Stores master stock information.

Fields:
- id
- symbol
- company_name
- exchange
- sector
- market_cap_category
- is_etf

---

### price_history

Stores historical OHLCV data.

Fields:
- id
- stock_id
- datetime
- open
- high
- low
- close
- volume

---

### predictions

Stores generated AI predictions.

Fields:
- id
- stock_id
- prediction_time
- horizon_minutes
- signal
- confidence_score
- target_price
- stop_loss
- risk_score

---

### users

Stores registered users.

Fields:
- id
- email
- name
- password_hash
- created_at

---

### watchlists

Stores user watchlists.

Fields:
- id
- user_id
- stock_id

---

### alerts

Stores alert subscriptions.

Fields:
- id
- user_id
- stock_id
- alert_type
- created_at