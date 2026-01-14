# FAQs on different Senarios

## How would you debug a performance issue where API responses are slow?

> **Interview goal:** They are NOT testing tools.
> They are testing **thinking, prioritization, and systems understanding**.

---

### 1️⃣ First: Clarify & Scope the Problem (VERY IMPORTANT)

Before touching code, I’d ask:

* Is the slowdown **constant or intermittent**?
* Is it **all APIs or specific endpoints**?
* Since when did it start? **Recent deployment?**
* Is it **for all users or specific regions/clients**?
* What’s the **expected vs actual latency**?

📌 This avoids blind debugging and shows maturity.

---

### 2️⃣ Check Metrics & Observability First (Not Code)

I start with **production metrics**, not local debugging.

#### Key metrics I look at:

* **Latency** (P50 / P90 / P99)
* **Error rate**
* **Request throughput**
* **CPU / Memory / Disk / Network usage**
* **DB connection pool usage**

If available, I use:

* APM tools (New Relic, Datadog, Elastic APM)
* Logs + traces

👉 This helps identify **where time is being spent**.

---

### 3️⃣ Identify the Bottleneck Layer

I mentally break the request lifecycle into layers:

```
Client
 → Load Balancer
 → API Gateway / Web Server
 → Application Code
 → Database / Cache / External Services
```

Then I isolate **which layer is slow**.

---

### 🔹 A. Application Layer Checks

I inspect:

* Slow functions / loops
* Blocking calls (sleep, retries, locks)
* Serialization overhead (JSON, large payloads)
* Thread / worker exhaustion

In Python/Django:

* Middleware timing
* View-level profiling
* N+1 queries triggered by ORM

---

### 🔹 B. Database Layer (VERY COMMON)

I check:

* Slow query logs
* Missing indexes
* N+1 query problem
* Long-running transactions
* Connection pool saturation

Example red flags:

```sql
SELECT * FROM orders WHERE user_id = ?
```

(no index 😬)

---

### 🔹 C. External Dependencies

If API calls:

* Third-party services
* Payment gateways
* Auth providers

I verify:

* Timeout configs
* Retry storms
* Circuit breakers
* Response times of dependencies

📌 One slow dependency can slow the whole API.

---

### 🔹 D. Caching Layer

I check:

* Cache hit vs miss ratio
* Cache TTLs
* Cache stampede
* Serialization cost

If cache miss rate is high → DB gets hammered.

---

## 4️⃣ Reproduce & Profile

Once I suspect a layer:

### Locally / staging:

* Reproduce using realistic data
* Load test using JMeter / Locust / k6

### Profile:

* CPU profiling
* Memory profiling
* Query profiling

Goal:

> **Prove** where the time is going.

---

## 5️⃣ Fix Strategically (Not Randomly)

Based on findings:

### Possible fixes:

* Add DB indexes
* Reduce queries (select_related / prefetch_related)
* Introduce caching
* Optimize payload size
* Move heavy tasks to async workers
* Add timeouts + circuit breakers
* Scale horizontally or vertically

📌 I always validate improvements using metrics.

---

## 6️⃣ Validate & Monitor After Fix

After deployment:

* Compare before vs after latency
* Monitor error rates
* Watch DB and CPU usage
* Add alerts for regression

---

## 7️⃣ Prevent It in the Future (Senior Touch)

I’d also mention:

* Add request tracing
* Add SLOs / SLAs
* Add performance tests in CI
* Add dashboards
* Document performance budgets

---

## Short, Crisp Interview Answer (2-minute version)

> “I start by scoping the issue and checking metrics like latency percentiles, error rates, and system usage. Then I isolate whether the bottleneck is in the application, database, cache, or external dependencies. I profile the slow path, identify root causes like N+1 queries or slow external calls, fix them with targeted optimizations, and finally validate the improvement using metrics and monitoring to prevent regressions.”

---

## Bonus: Common interviewer follow-ups

**Q:** What’s the most common cause of slow APIs?
👉 Database queries (indexes, N+1, bad joins)

**Q:** How do you know it’s not infra?
👉 CPU/memory/network metrics + request tracing

**Q:** Threads vs async?
👉 Async for I/O-bound, multiprocessing for CPU-bound

