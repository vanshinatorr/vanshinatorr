<div align="center">

<img src="./architecture_schematic.svg" width="100%" alt="Vansh Vijay Banner" />

<br/><br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=24&pause=1000&color=A78BFA&center=true&vCenter=true&width=750&lines=Building+real+products%2C+not+just+projects.;MERN+Stack+%7C+REST+APIs+%7C+WebSockets;Founder+of+ConsistPay+(Active+production+userbase);Solving+DSA+consistently+(300%2B+problems);Consistency+compounds.)](https://git.io/typing-svg)

<br/><br/>

<img src="https://vanshvijay.me/api/telemetry/live" width="100%" alt="Live System Telemetry" />

<br/><br/>

</div>

---

# SYSTEM SPECIFICATION: VANSH VIJAY

---

### Core Configuration

> **Candidate:** Vansh Vijay (Full-Stack & Backend Systems)  
> **University:** B.Tech CSE (2023 - 2027) @ JECRC University, Jaipur  
> **Core Stack:** Node.js / Express.js / React.js / MongoDB / C++  
> **Strategy:** 1500+ Peak ELO (Chess.com strategic matchmaking)  
> **Status:** **ACTIVE_FOR_HIRING** (Open to SDE Internships / Roles)

---

### Production Modules

<table width="100%">
<tr>
<td>

### `module/consistpay` — Coding Streak Platform (Live)
> [Live Platform](https://daily-coding-habit-tracker.vercel.app) • [Source Code](https://github.com/vanshinatorr/Daily-coding-habit-tracker)

A production-deployed application designed to solve developer inconsistency using financial accountability stakes. Used by **60+ active users**.

**Technical Implementations:**
*   **Concurrency:** Resolved data-race bugs on check-ins using unique database indexes and atomic MongoDB operators (`$set`, `$setOnInsert`).
*   **Integration:** Designed a retry-tolerant webhook receiver for Razorpay payments, guaranteeing transaction data integrity during server down sequences.
*   **Feedback:** Linked Google Gemini API to analyze developer progress logs and output personalized habit reports.

**Telemetry Specs:**
*   **Query Latency:** `< 5ms` database execution on index-optimized log lookups.
*   **Request Load:** Scaled to handle `100+ req/sec` using in-memory queues.

</td>
</tr>
</table>

---

<table width="100%">
<tr>
<td>

### `module/chess-multiplayer` — Real-Time Game Lobby
> [Play Live Game](https://chess-multiplayer-y54n.onrender.com) • [Source Code](https://github.com/vanshinatorr/chess-multiplayer)

A low-latency multiplayer chess platform with dynamic room codes and matchmaking.

**Technical Implementations:**
*   **Caching:** Cached lobby and active game sessions in custom in-memory JavaScript maps instead of persistent database writes, reducing processing latency.
*   **Resilience:** Engineered server-side match state serialization to restore active game clocks and players' connections during brief network drops.

**Telemetry Specs:**
*   **Sync Latency:** Sub-`15ms` real-time move synchronization via custom Socket.IO packets.
*   **Payload Size:** Optimized JSON packets to keep data transfers under `200 bytes` per move.

</td>
</tr>
</table>

---

<table width="100%">
<tr>
<td>

### `module/telemetry-cache-streamer` — System Metric Spooler
> [Source Code](https://github.com/vanshinatorr/telemetry-cache-streamer)

A background utility in C++17 to buffer, throttle, and serialize system telemetry metrics.

**Technical Implementations:**
*   **Locking Strategy:** Implemented a thread-safe circular buffer with mutex synchronization, reducing thread blocking states by 78% via double-buffer asynchronous writing.
*   **Resource Bounds:** Bounded maximum heap utilization strictly to 16MB configuration limits to prevent memory leaks in resource-constrained target environments.

**Telemetry Specs:**
*   **Heap Limit:** Capped strictly to `16MB` memory footprint.
*   **Thread Blocking:** Reduced thread block states by 78% compared to single-mutex structures.

</td>
</tr>
</table>

---

### Contact & Candidate API Endpoints

<table width="100%">
<tr>
<td>

**How to Connect:**
*   **If you are a Recruiter / HR:** Click here to [**Email me directly**](mailto:vanshvijay9784@gmail.com) or connect on [**LinkedIn**](https://www.linkedin.com/in/vansh-vijay/). (Zero steps required!)
*   **If you are a Developer / Tech Lead:** Copy the commands below to query my live metadata or send a hire ping directly to my Discord via your terminal!

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

---

### Runtime Metrics & Analytics

<p align="center">
  <img src="https://streak-stats.demolab.com?user=vanshinatorr&theme=tokyonight&hide_border=true&date_format=j%20M%5B%20Y%5D" width="49%" />
  <img src="./skills_radar.svg" width="49%" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=vanshinatorr&bg_color=0d1117&color=a78bfa&line=7c3aed&point=c4b5fd&area=true&hide_border=true&custom_title=Contribution%20Activity" width="99%" />
</p>

---

<div align="center">
  <br/>
  
  `[ `[LinkedIn](https://www.linkedin.com/in/vansh-vijay/)` ]`  •  `[ `[Twitter](https://x.com/vanshvijay9)` ]`  •  `[ `[Email](mailto:vanshvijay9784@gmail.com)` ]`

  <br/><br/>
  
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%"/>
</div>
