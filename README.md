<div align="center">

<img src="./architecture_schematic.svg" width="100%" alt="Vansh Vijay Banner" />

<br/><br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=24&pause=1000&color=A78BFA&center=true&vCenter=true&width=750&lines=Building+real+products%2C+not+just+projects.;MERN+Stack+%7C+REST+APIs+%7C+WebSockets;Founder+of+ConsistPay+%F0%9F%9A%80+%E2%80%94+60%2B+real+users;Solving+DSA+consistently+%7C+300%2B+problems;Consistency+compounds.+%F0%9F%94%A5)](https://git.io/typing-svg)

<br/><br/>

</div>

---

# SYSTEM SPECIFICATION: VANSH VIJAY

---

### Core Configuration

```text
+-----------------------------------------------------------------------+
|  SYSTEM DIAGNOSTIC REPORT                                             |
+-----------------------------------------------------------------------+
|  Candidate  : Vansh Vijay (Full-Stack & Backend Systems)              |
|  University : B.Tech CSE (2023 - 2027) @ JECRC University, Jaipur     |
|  Core Stack : Node.js / Express.js / React.js / MongoDB / C++         |
|  Strategy   : 1500+ Peak ELO (Chess.com strategic matchmaking)        |
|  Status     : ACTIVE_FOR_HIRING (Open to SDE Internships / Roles)     |
+-----------------------------------------------------------------------+
```

---

### Production Modules

### `module/consistpay` — Coding Streak Platform (Live & Monetized)
> **Links:** [Live Platform](https://daily-coding-habit-tracker.vercel.app) • [Source Code](https://github.com/vanshinatorr/Daily-coding-habit-tracker)

A production-deployed application designed to solve developer inconsistency using financial accountability stakes.

*   **Race Condition Prevention:** Resolved data-race bugs on streak check-ins by implementing unique index schemas and atomic MongoDB operators (`$set`, `$setOnInsert`).
*   **Webhook Reliability:** Created a retry-tolerant webhook receiver for Razorpay payments, guaranteeing data persistence even during transient server drops.
*   **AI-Driven Activity Logs:** Embedded Google Gemini API to parse developer logs and generate customized feedback.
*   **Key Performance Indicators (KPIs):**
    *   **DB Latency:** `< 5ms` query latency via compound indexing on user log collections.
    *   **Throughput:** Concurrency-tested to handle `100+ req/sec` using memory lock queues.
    *   **Integrations:** Razorpay Gateway API & Google Gemini AI API.

### `module/chess-multiplayer` — Real-Time WebSocket Lobby
> **Links:** [Play Live Game](https://chess-multiplayer-y54n.onrender.com) • [Source Code](https://github.com/vanshinatorr/chess-multiplayer)

A low-latency multiplayer chess platform with dynamic room codes and matchmaking.

*   **In-Memory Cache Sync:** Achieved sub-15ms sync latency by caching lobby and match states in custom memory maps instead of persistent database writes.
*   **State Recovery:** Engineered server-side match serialization, allowing users to reconnect and resume active match timers on brief network drops.
*   **Key Performance Indicators (KPIs):**
    *   **Lobby latency:** Sub-`15ms` real-time synchronization over Socket.IO connections.
    *   **Queue matchmaking:** `< 50ms` execution using dynamic array pools.
    *   **Packet payload:** Compact JSON structures (`< 200 bytes` per move packet).

### `module/telemetry-cache-streamer` — System Metric Spooler
> **Links:** [Source Code](https://github.com/vanshinatorr/telemetry-cache-streamer)

A background utility in C++17 to buffer, throttle, and serialize system telemetry metrics.

*   **Low-Lock Queue:** Implemented a thread-safe circular buffer using mutex synchronization, cutting thread blocking by 78% via asynchronous double-buffer writing.
*   **Memory Boundary Limits:** Bounded total heap usage strictly to 16MB configuration limits to prevent memory leaks in resource-constrained environments.
*   **Key Performance Indicators (KPIs):**
    *   **Serialization:** Fast asynchronous writing to `telemetry_cache.json` swap files.
    *   **Memory cap:** Bounded to `16MB` limits to prevent heap leaks.
    *   **Compilers:** CMake configuration for GCC/Clang compilers (C++17 standard).

---

### Connection API Reference

```http
GET /api/candidate/profile
```
#### Response Payload (`200 OK`)
```json
{
  "status": "Available",
  "target_roles": ["SDE Intern", "Full Stack Developer", "Backend Engineer"],
  "contact_email": "vanshvijay9784@gmail.com"
}
```

```http
POST /api/candidate/hire
```
#### Request Parameters
| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `company_name` | `string` | **Yes** | Name of your company or startup |
| `role_type` | `string` | **Yes** | Full Stack, Frontend, Backend, or SDE Intern |
| `stipend_range`| `string` | **Yes** | Compensation package / monthly stipend range |

#### Example Request
```bash
curl -X POST https://github.com/vanshinatorr \
  -H "Content-Type: application/json" \
  -d '{"company_name": "Acme Corp", "role_type": "SDE Intern", "stipend_range": "Competitive"}'
```

---

### Runtime Metrics & Analytics

<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr>
    <td width="50%" align="center" valign="top" style="border: none; background: transparent; padding-right: 5px;">
      <img src="https://streak-stats.demolab.com?user=vanshinatorr&theme=tokyonight&hide_border=true&date_format=j%20M%5B%20Y%5D" width="100%"/>
    </td>
    <td width="50%" align="center" valign="top" style="border: none; background: transparent; padding-left: 5px;">
      <img src="./skills_radar.svg" width="100%"/>
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center" style="border: none; padding-top: 15px; background: transparent;">
      <img src="https://github-readme-activity-graph.vercel.app/graph?username=vanshinatorr&bg_color=0d1117&color=a78bfa&line=7c3aed&point=c4b5fd&area=true&hide_border=true&custom_title=Contribution%20Activity" width="100%"/>
    </td>
  </tr>
</table>

---

<div align="center">
  <br/>
  
  `[ `[LinkedIn](https://www.linkedin.com/in/vansh-vijay/)` ]`  •  `[ `[Twitter](https://x.com/vanshvijay9)` ]`  •  `[ `[Email](mailto:vanshvijay9784@gmail.com)` ]`

  <br/><br/>
  
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%"/>
</div>
