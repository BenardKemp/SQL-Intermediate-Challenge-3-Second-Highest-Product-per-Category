# SQL Intermediate Challenge #3: Second-Highest Product per Category

**Difficulty:** Intermediate  
**Estimated time:** 30–40 minutes  
**Concepts:** correlated subqueries, ordering with offsets, tie handling, optional window functions  

This challenge builds directly on “Top Product per Category” and introduces a harder, more realistic problem: finding the **second-highest value per group**.

---

## 🧠 The Challenge

**The product manager asks:**

> “For each category, which product is the second most expensive?”

This is deceptively difficult:
- You can’t solve it with `MAX()` alone
- You must define a clear ordering
- You must handle ties deterministically

---

## 📊 Table Schema

### `products`

| Column Name | Type | Description |
|------------|------|-------------|
| product_id | INTEGER | Unique product ID |
| name | TEXT | Product name |
| category | TEXT | Product category |
| price | DECIMAL | Product price |

---

## 🧪 Sample Data (Includes Ties)

| product_id | name | category | price |
|-----------:|------|----------|------:|
| 201 | Wireless Mouse | Accessories | 24.99 |
| 202 | Mechanical Keyboard | Accessories | 89.00 |
| 203 | Pro Keyboard | Accessories | 89.00 |
| 204 | USB-C Hub | Accessories | 34.50 |
| 205 | Monitor | Displays | 229.99 |
| 206 | 34-inch Monitor | Displays | 399.00 |
| 207 | Desk Lamp | Workspace | 49.99 |
| 208 | Chair Mat | Workspace | 79.99 |

---

## ✍️ Your Task

Return **one row per category** with:

- `category`
- `name`
- `price`

Where the product is the **second-highest priced** in that category.

### Tie rule (required)

Within each category:
1. Sort by `price DESC`
2. Break ties with `product_id ASC`
3. Select the **second row**

Sort final results by:
- `category` (A–Z)

---

## 🧩 Expected Output

| category | name | price |
|---------|------|------:|
| Accessories | Pro Keyboard | 89.00 |
| Displays | Monitor | 229.99 |
| Workspace | Desk Lamp | 49.99 |

---

## ✅ Requirements

Your query must:

- Return **exactly one row per category**
- Follow the tie-breaking rule
- Not use `SELECT *`
- Work correctly even when prices are duplicated

---

## 💡 Hint (Optional)

“Second highest” usually means:
- Sort rows **within each group**
- Skip the first row
- Select the next one

You can do this using:
- a **correlated subquery** (SQLite-safe)
- or a **window function** like `ROW_NUMBER()`

---

## 🧪 Write Your SQL Here

```sql
-- Write your query here

