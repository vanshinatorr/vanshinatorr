<div align="center">

<img src="./architecture_schematic.svg" width="100%" alt="Vansh Vijay Banner" />

<br/><br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=24&pause=1000&color=A78BFA&center=true&vCenter=true&width=750&lines=Building+real+products%2C+not+just+projects.;MERN+Stack+%7C+REST+APIs+%7C+WebSockets;Founder+of+ConsistPay+%F0%9F%9A%80+%E2%80%94+60%2B+real+users;Solving+DSA+consistently+%7C+300%2B+problems;Consistency+compounds.+%F0%9F%94%A5)](https://git.io/typing-svg)

<br/><br/>

</div>

---

# 📂 WORKSPACE EXPLORER

> Click on the folders and files below to expand their contents.

<details open>
<summary><b>📁 system_config</b></summary>

<details style="margin-left: 20px;">
<summary>📄 <code>spec_sheet.ts</code> (Candidate Metadata)</summary>

```ts
// spec_sheet.ts
const candidate: Developer = {
  name: "Vansh Vijay",
  university: "JECRC University, Jaipur — B.Tech CSE (2023–2027)",
  focus: "High-Performance Backends & Clean UI",
  coreStack: ["Node.js", "Express.js", "React.js", "MongoDB"],
  achievements: {
    codolio: "Top 30 Coding Profiles at JECRC (among 2000+ students)",
    dsa: "300+ Solved problems (LeetCode & GFG in C++)",
    chess: "1500+ peak ELO (Strategic chess thinker)"
  }
};
```

</details>

</details>

<details open>
<summary><b>📁 featured_modules</b></summary>

<details style="margin-left: 20px;">
<summary>📄 <code>consistpay.md</code> (MERN Stack + Gemini AI)</summary>

### ⚡ ConsistPay — Coding Accountability Platform
> **Links:** [Live Site](https://daily-coding-habit-tracker.vercel.app) | [Source Code](https://github.com/vanshinatorr/Daily-coding-habit-tracker)

A live app used by **60+ active users** to maintain daily coding habits. 

**What I solved:**
- **Double-Streak Bug:** Fixed a race condition where multiple rapid requests would double-claim streaks or payments, by implementing MongoDB uniqueness locks and atomic `$set` operations.
- **Webhook Resilience:** Integrated Razorpay webhooks with retries. If our server goes down momentarily during a payment, the transaction isn't lost—it retries and updates the user's streak safely.
- **AI Activity Review:** Hooked up the Gemini API to analyze user logs and generate dynamic feedback on their progress.

</details>

<details style="margin-left: 20px;">
<summary>📄 <code>chess_multiplayer.md</code> (Node.js + Socket.IO)</summary>

### ♟️ Chess Multiplayer — Real-time WebSockets
> **Links:** [Play Live](https://chess-multiplayer-y54n.onrender.com) | [Source Code](https://github.com/vanshinatorr/chess-multiplayer)

A real-time chess platform with room creation and matchmaking. Built in a day.

**What I solved:**
- **Under-15ms Latency:** Instead of querying MongoDB for every move, I stored active room sessions in-memory using JavaScript maps. This keeps game play fast and lag-free.
- **Connection Recovery:** Stored game states on the server so that if a player's internet drops, they can reconnect to the same match and resume their timer without losing progress.

</details>

<details style="margin-left: 20px;">
<summary>📄 <code>telemetry_cache_streamer.md</code> (C++17 System Daemon)</summary>

### ⚙️ Telemetry Cache Streamer — High-Performance C++17 Utility
> **Links:** [Source Code](https://github.com/vanshinatorr/telemetry-cache-streamer)

A local background utility built in C++17 to buffer, throttle, and serialize system telemetry metrics before they are pushed upstream.

**What I solved:**
- **78% Less Thread Blocking:** Avoided standard queue lock bottlenecks by implementing a double-buffered circular memory structure. While one buffer ingests metrics, the other is flushed to disk asynchronously.
- **Deterministic Memory:** Capped the daemon's memory footprint strictly to 16MB to ensure it never causes memory leaks or crashes on small, resource-constrained servers.

</details>

</details>

<details open>
<summary><b>📁 candidate_endpoints</b></summary>

<details style="margin-left: 20px;">
<summary>📄 <code>hire_api.http</code> (Mock REST endpoint definitions)</summary>

### 📬 SDE Candidate API Reference

```http
GET /api/candidate/profile
```
#### Response Payload (`200 OK`)
```json
{
  "status": "Available",
  "target_roles": ["SDE Intern", "Full Stack Developer", "Backend Engineer"],
  "current_locations": ["Jaipur, India", "Remote"],
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

</details>

</details>

<details open>
<summary><b>📁 telemetry_analytics</b></summary>

<details style="margin-left: 20px;">
<summary>📄 <code>activity_charts.md</code> (GitHub status logs)</summary>

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

</details>

</details>

---

<div align="center">
  <br/>
  <a href="https://www.linkedin.com/in/vansh-vijay/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin"/></a>
  <a href="https://x.com/vanshvijay9"><img src="https://img.shields.io/badge/Twitter-Follow-000000?style=for-the-badge&logo=x"/></a>
  <a href="mailto:vanshvijay9784@gmail.com"><img src="https://img.shields.io/badge/Email-Reach%20Out-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <br/><br/>
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%"/>
</div>
