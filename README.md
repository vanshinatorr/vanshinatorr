
<div align="center">

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=19&pause=1000&duration=4000&color=38BDF8&center=true&vCenter=true&width=800&height=45&lines=MERN+%2F+Java+Full-Stack+Developer;Building+ConsistPay;300%2B+DSA+Problems+Solved;Learning+by+Building+Real+Projects" width="100%" alt="Vansh Vijay — Full-Stack Developer" />
</a>

<img src="./architecture_schematic.svg?v=7" width="100%" alt="Vansh Vijay — Java and MERN Full-Stack Developer" />

</div>

---

## Engineering Projects

<table width="100%">
<tr>
<td>

### `module/consistpay` — Streak Accountability Platform (Live)

> [Live Deployment](https://daily-coding-habit-tracker.vercel.app/) • [Source Code](https://github.com/vanshinatorr/Daily-coding-habit-tracker)

**Operational Context:**

- A production accountability application designed to enforce developer consistency using financial stakes. Currently serving **100+ active users**.

**Engineering Solves:**

- **Concurrency Locks:** Prevented duplicate check-in streak claims by implementing unique database index constraints and atomic MongoDB operators (`$set`, `$setOnInsert`).
- **Transaction Persistence:** Designed a retry-tolerant Razorpay webhook receiver to guarantee transaction data consistency during transient server outages.
- **LLM Integration:** Connected Google Gemini AI to analyze daily activity logs and write dynamic progress reports.

**System Telemetry:**

- **Database Latency:** `< 5ms` execution on index-optimized log queries.
- **Transaction Throughput:** Stress-tested to handle `100+ req/sec` using in-memory queues.

</td>
</tr>
</table>

<table width="100%">
<tr>
<td>

### `module/chess-multiplayer` — Real-Time WebSocket Lobby

> [Play Live Game](https://chess-multiplayer-y54n.onrender.com/) • [Source Code](https://github.com/vanshinatorr/chess-multiplayer)

**Operational Context:**

- A low-latency multiplayer chess platform featuring dynamic room codes and matchmaking.

**Engineering Solves:**

- **Lobby Cache:** Stored active room metadata and game states in custom in-memory JavaScript maps to bypass heavy persistent database read/write bottlenecks.
- **State Recovery:** Designed server-side session serialization to restore active game clocks and players' connection states during network dropouts.

**System Telemetry:**

- **Sync Latency:** Sub-`15ms` real-time synchronization over Socket.IO connections.
- **Payload Size:** Optimized JSON packets to keep data transfers under `200 bytes` per move.

</td>
</tr>
</table>

<table width="100%">
<tr>
<td>

### `module/telemetry-cache-streamer` — High-Performance Metric Spooler

> [Source Code](https://github.com/vanshinatorr/telemetry-cache-streamer)

**Operational Context:**

- A background system daemon in C++17 to buffer, throttle, and serialize system telemetry metrics.

**Engineering Solves:**

- **Lock Contention:** Reduced thread blocking states by 78% by implementing a double-buffered circular memory queue with mutex-locked asynchronous disk writes.
- **Heap Boundaries:** Bounded maximum memory usage strictly to 16MB configuration limits to prevent leaks on resource-constrained servers.

**System Telemetry:**

- **Memory Footprint:** Bounded strictly to `16MB` memory limits.
- **Queue Performance:** 78% reduction in block states compared to single-mutex structures.

</td>
</tr>
</table>

---

## Experience

<table width="100%">
<tr>
<td>

### The Solution Consultancy — Full-Stack Intern

**April 2026 – September 2026 · Jaipur, India**

- Internship exposure to Java, Spring Boot, REST APIs, and MySQL.
- Learned how backend requests, database persistence, and API testing fit together in an application workflow.
- Gained exposure to application structure, record management, and API testing with Postman.

</td>
</tr>
<tr>
<td>

### Plasmid Innovation — Full-Stack Intern

**August 2025 – September 2025**

- Worked with Node.js, Express.js, MongoDB, and Mongoose.
- Learned REST API development and CRUD operations through employee and leave management workflows.
- Gained experience with basic frontend-backend integration.

</td>
</tr>
</table>

---

## Contact Me

<div align="center">

<table>
<tr>
<td align="center">

<sub>COMMUNICATION INTERFACES</sub>

### `❯ npx vansh-vijay`

<sub>Run in terminal</sub>

<br/>

<a href="mailto:vanshvijay9784@gmail.com"><img src="https://img.shields.io/badge/Email-1e293b?style=for-the-badge&logo=gmail&logoColor=38bdf8" alt="Email" /></a>

</td>
</tr>
</table>

</div>

---

<div align="center">

<table width="100%">
<tr>
<td width="50%" align="center">
  <img src="./capability_matrix_v4.svg?v=7" width="100%" alt="Full-Stack Capability Matrix" />
</td>
<td width="50%" align="center">
  <img src="./streak_stats.svg?v=7" width="100%" alt="GitHub Contribution and Streak Statistics" />
</td>
</tr>
</table>

</div>

---

<div align="center">

[LinkedIn](https://www.linkedin.com/in/vansh-vijay/) · [X](https://x.com/vanshvijay9) · [Email](mailto:vanshvijay9784@gmail.com)

</div>
