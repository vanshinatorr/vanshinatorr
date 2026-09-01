<div align="center">

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=700&amp;size=19&amp;pause=1000&amp;duration=4000&amp;color=38bdf8&amp;center=true&amp;vCenter=true&amp;width=800&amp;height=40&amp;lines=MERN+%2F+Full-Stack+Developer;ConsistPay%3A+Streak+accountability+platform.;300%2B+DSA+Problems+Solved+in+C%2B%2B.;Building+real+products%2C+not+just+projects." width="100%" alt="Typing SVG" />
</a>

<img src="https://vanshvijay.me/api/telemetry/live?v=12" width="100%" alt="Vansh Vijay System Architecture &amp; Telemetry" />

</div>
<h3 align="center">Production Modules</h3>
<table width="100%">
<tr>
<td>

### `module/consistpay` — Streak Accountability Platform (Live)
> [Live Deployment](https://daily-coding-habit-tracker.vercel.app) • [Source Code](https://github.com/vanshinatorr/Daily-coding-habit-tracker)

**Operational Context:**
*   A production accountability application designed to enforce developer consistency using financial stakes. Currently serving **100+ active users**.

**Engineering Solves:**
*   **Concurrency Locks:** Prevented duplicate check-in streak claims by implementing unique database index constraints and atomic MongoDB operators (`$set`, `$setOnInsert`).
*   **Transaction Persistence:** Designed a retry-tolerant Razorpay webhook receiver to guarantee transaction data consistency during transient server outages.
*   **LLM Integration:** Connected Google Gemini AI to analyze daily activity logs and write dynamic progress reports.

**System Telemetry:**
*   **Database Latency:** `< 5ms` execution on index-optimized log queries.
*   **Transaction Throughput:** Stress-tested to handle `100+ req/sec` using in-memory queues.

</td>
</tr>
</table>

<table width="100%">
<tr>
<td>

### `module/chess-multiplayer` — Real-Time WebSocket Lobby
> [Play Live Game](https://chess-multiplayer-y54n.onrender.com) • [Source Code](https://github.com/vanshinatorr/chess-multiplayer)

**Operational Context:**
*   A low-latency multiplayer chess platform featuring dynamic room codes and matchmaking.

**Engineering Solves:**
*   **Lobby Cache:** Stored active room metadata and game states in custom in-memory JavaScript maps to bypass heavy persistent database read/write bottlenecks.
*   **State Recovery:** Designed server-side session serialization to restore active game clocks and players' connection states during network dropouts.

**System Telemetry:**
*   **Sync Latency:** Sub-`15ms` real-time synchronization over Socket.IO connections.
*   **Payload Size:** Optimized JSON packets to keep data transfers under `200 bytes` per move.

</td>
</tr>
</table>

<table width="100%">
<tr>
<td>

### `module/telemetry-cache-streamer` — High-Performance Metric Spooler
> [Source Code](https://github.com/vanshinatorr/telemetry-cache-streamer)

**Operational Context:**
*   A background system daemon in C++17 to buffer, throttle, and serialize system telemetry metrics.

**Engineering Solves:**
*   **Lock Contention:** Reduced thread blocking states by 78% by implementing a double-buffered circular memory queue with mutex-locked asynchronous disk writes.
*   **Heap Boundaries:** Bounded maximum memory usage strictly to 16MB configuration limits to prevent leaks on resource-constrained servers.

**System Telemetry:**
*   **Memory Footprint:** Bounded strictly to `16MB` memory limits.
*   **Queue Performance:** 78% reduction in block states compared to single-mutex structures.

</td>
</tr>
</table>

---

### Contact Me

<div align="center">
<table width="100%">
<tr>
<td align="center">

<sub>COMMUNICATION INTERFACES</sub>

### `❯ npx vansh-vijay`

<sub>Run in terminal</sub>

<br/><br/>

<a href="https://www.linkedin.com/in/vansh-vijay/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-1e293b?style=for-the-badge&amp;logo=linkedin&amp;logoColor=38bdf8" alt="LinkedIn" /></a> &nbsp;&nbsp;&nbsp;&nbsp; <a href="mailto:vanshvijay9784@gmail.com"><img src="https://img.shields.io/badge/Email-1e293b?style=for-the-badge&amp;logo=gmail&amp;logoColor=38bdf8" alt="Email" /></a>

</td>
</tr>
</table>
</div>

---

<table width="100%">
<tr>
<td width="50%" align="center">
  <img src="./capability_matrix_v4.svg?v=6" width="100%" alt="Expertise" />
</td>
<td width="50%" align="center">
  <img src="./streak_stats.svg?v=6" width="100%" alt="GitHub Streak Stats" />
</td>
</tr>
</table>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=vanshinatorr&bg_color=0d0e12&color=38bdf8&line=38bdf8&point=38bdf8&area=true&hide_border=true&custom_title=Contribution+Activity" width="100%" />
</p>

---

<div align="center">
  <br/>
  
  [LinkedIn](https://www.linkedin.com/in/vansh-vijay/) &nbsp;•&nbsp; [Twitter](https://x.com/vanshvijay9) &nbsp;•&nbsp; [Email](mailto:vanshvijay9784@gmail.com)
</div>
