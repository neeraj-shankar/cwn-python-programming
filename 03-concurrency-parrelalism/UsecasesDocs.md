# Common Use cases based on Concurrency and Parralelism

# Concurrency Control through Locking Strategies

## The Core Problem: The Race Condition

1. User 1 checks if seats 2, 3, and 4 are free. (System says: Yes).
2. User 2 checks if seats 3, 4, and 5 are free. (System says: Yes).
3. User 1 writes "Booked" to seats 2, 3, and 4.
4. User 2 writes "Booked" to seats 3, 4, and 5.

- **Result:** Seat 3 and 4 are double-booked. This is a failure of Atomicity (the "A" in ACID database properties).

### Solution A: Pessimistic Locking

#### 1. **How it works:** When User 1 queries seats 2, 3, and 4, the database puts a "Lock" on those specific rows `(e.g., SELECT ... FOR UPDATE)`.

#### **2. The Result:** If User 2 tries to even look at seat 3 while User 1 is still in the middle of their transaction, User 2’s request is put on hold (blocked). They have to wait until User 1 finishes or times out.

#### **3. Pros:** Guaranteed consistency. No double booking.

#### **4. Cons:** Slows down the system. If User 1 has a slow internet connection during checkout, those seats stay locked for everyone else.

### Solution B: Optimistic Locking (Versioning)
This assumes that conflicts are rare and uses a Version Number or Timestamp to catch errors.

#### **How it works:** 
- 1. Both users read the seats and see version: 1.
- 2. User 1 submits their booking: "Update seat 3, set status='booked' where version=1."
- 3. The update succeeds, and the system bumps the version to 2.
- 4. User 2 submits their booking: "Update seat 3, set status='booked' where version=1."
- 5. The Fail: The database sees that the version is now 2, not 1. It rejects User 2’s request.

#### **The Result**: User 2 gets an error message: "Sorry, these seats were just taken!"

#### **Pros:** Very fast; doesn't hold up the database.

#### **Cons:** User 2 might be frustrated because they thought the seats were available until the very last click.

### Solution C: Distributed Locking (Redis/Redlock)
In a massive system like BookMyShow, you likely have multiple web servers and multiple database instances. A standard database lock might not be enough.

#### **How it works:** 
- You use a fast, in-memory store like **Redis**. Before a user can even start the checkout process, the application tries to set a "Key" in Redis: `lock:seat:3`.

- If User 1 gets the key first, User 2’s attempt to "Set" that key fails immediately.

#### **The Result:** 
This is often how "Expired in 10:00 minutes" timers work. You "hold" the seat in a distributed cache while the user enters their credit card info.


## Thread Kill Problem
To understand what happens when a **thread dies**, we have to look at how it dies.

### Scenario A: The Thread **"Exits"** Gracefully
If a thread in P1 finishes its work or hits a return statement, it simply terminates.

- **Impact on P1:** None. The other 3 threads continue running normally. The process stays alive.
- **Impact on P2:** Absolutely none. Processes are isolated from one another.

### Scenario B: The Thread Crashes (Segmentation Fault/Exception)
This is the most common "killed" scenario. If a thread performs an illegal operation (like accessing memory it doesn't own or dividing by zero) and the error isn't caught:

#### **Impact on P1:** 
The entire process (P1) usually crashes. In most operating systems (Unix/Linux/Windows), a fatal signal (like `SIGSEGV` or `SIGILL`) is delivered to the process. Since all threads share the same memory space and signal handlers, the OS terminates the parent process to prevent memory corruption.

### **The Remaining Threads in P1:** They are killed instantly. When the process dies, the OS reclaims the memory and closes all threads associated with it.

### **Impact on P2:** Zero. P2 lives in its own "sandbox." This is the beauty of process isolation; a crash in one does not leak into the other.

### Scenario C: An External Tool Kills the Thread
If you use a debugger or a specific OS call to "cancel" or "kill" a specific Thread ID (TID) without hitting a fatal error:

- **Impact on P1:** P1 stays alive.

- **The Remaining Threads in P1:** They survive, but they might be in a **"Zombie"** or **"Deadlocked"** state.

- **The Danger:** If the killed thread was holding a Mutex (Lock), it might never release it. The remaining threads will eventually try to acquire that lock and hang forever. This is why "killing" threads manually is considered very dangerous in programming.

- **Impact on P2:** Still none.
