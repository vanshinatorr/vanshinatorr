<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=21&pause=1000&duration=4000&color=38bdf8&center=true&vCenter=true&width=800&height=40&lines=Building+backends%2C+API+pipelines%2C+and+real-time+apps.;ConsistPay%3A+Streak+accountability+platform+(60%2B+users).;Core+Stack%3A+Node.js+%2F%2F+Express.js+%2F%2F+React.js+%2F%2F+C%2B%2B.;Solving+DSA+consistently+(300%2B+problems+in+C%2B%2B).;Building+scalable+products%2C+not+just+simple+projects.)](https://git.io/typing-svg)

<br/><br/>

<img src="./architecture_schematic.svg" width="100%" alt="Vansh Vijay Banner" />

<br/>

<img src="https://vanshvijay.me/api/telemetry/live" width="100%" alt="Live System Telemetry" />

<br/><br/>

</div>

---

### Production Modules

<table width="100%">
<tr>
<td>

### `module/consistpay` — Streak Accountability Platform (Live)
> [Live Deployment](https://daily-coding-habit-tracker.vercel.app) • [Source Code](https://github.com/vanshinatorr/Daily-coding-habit-tracker)

**Operational Context:**
*   A production accountability application designed to enforce developer consistency using financial stakes. Currently serving **60+ active users**.

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

---

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

---

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

### Contact & Candidate API Endpoints

<table width="100%">
<tr>
<td>

**Connection Routing:**
*   **Recruiter Pipeline (Non-Technical):** Click here to [**Email me directly**](mailto:vanshvijay9784@gmail.com) or connect on [**LinkedIn**](https://www.linkedin.com/in/vansh-vijay/). (Zero steps required!)
*   **Developer Interface (Technical):** Copy the commands below to query my live metadata or send a hire ping directly to my Discord via your terminal!

</td>
</tr>
</table>

```http
GET https://vanshvijay.me/api/candidate/profile
```
#### Example Request
```bash
curl -s https://vanshvijay.me/api/candidate/profile | json_pp
```

#### Response Payload
```http
HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *

{
  "status": "Available",
  "target_roles": ["SDE Intern", "Full Stack Developer", "Backend Engineer"],
  "contact_email": "vanshvijay9784@gmail.com"
}
```

```http
POST https://vanshvijay.me/api/candidate/hire
```
#### Request Parameters
| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `company_name` | `string` | **Yes** | Name of your company or startup |
| `role_type` | `string` | **Yes** | Full Stack, Frontend, Backend, or SDE Intern |
| `stipend_range`| `string` | **Yes** | Compensation package / monthly stipend range |

#### Example Request
```bash
curl -s -X POST https://vanshvijay.me/api/candidate/hire \
  -H "Content-Type: application/json" \
  -d '{"company_name": "Acme Corp", "role_type": "SDE Intern", "stipend_range": "Competitive"}' | json_pp
```

#### Response Payload
```http
HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *

{
  "status": "Success",
  "message": "Hire request received from Acme Corp for the SDE Intern role! Connection initialized.",
  "candidate_notification": "Sent",
  "contact_email": "vanshvijay9784@gmail.com",
  "timestamp": "2026-08-19T02:00:00.000Z"
}
```

### Runtime Metrics & Analytics

<p align="center">
  <img src="https://streak-stats.demolab.com?user=vanshinatorr&background=0d0e12&border=1e293b&stroke=334155&ring=38bdf8&fire=38bdf8&currStreakNum=e2e8f0&sideNums=cbd5e1&sideLabels=94a3b8&dates=64748b&hide_border=true&date_format=j%20M%5B%20Y%5D" width="49%" />
  <img src="./skills_radar.svg" width="49%" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=vanshinatorr&bg_color=0d0e12&color=38bdf8&line=38bdf8&point=38bdf8&area=true&hide_border=true&custom_title=Contribution+Activity" width="99%" />
</p>

---

<div align="center">
  <br/>
  
  [LinkedIn](https://www.linkedin.com/in/vansh-vijay/) &nbsp;•&nbsp; [Twitter](https://x.com/vanshvijay9) &nbsp;•&nbsp; [Email](mailto:vanshvijay9784@gmail.com)
</div>
