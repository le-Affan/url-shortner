# Check Point Notes:

### 6 Oct:
- URL shortening logic with alias, custom domain and clash checks is complete.
- Looking into learning more about FastAPI to build the actual app now.

### 9 Oct:
- you were writing the function which builds the whole url but this time with actual DB lookups and shit. 

### 10 Oct:
- fast API end point which takes in long URL with optional alias and custom domain and gives short URL is now working.
- next up is gonna be completing the other FR

### 15 Oct:
- added 'expires_at' and 'clicks' to the urls table and created a new analytics tables containing 'url_id' and 'accessed_at' for FR-6 (The system can track basic analytics such as click count and access time)

### 19 Oct:
- completed all FRs.
- moving to NFRs and overall system design.


# Design Decisions:
- 2 DB tables: urls and analytics
- at every click, the link is first checked for validty. If the 'expires_at' timestamp has passed, the link is then disabled and a message 'link not found or has expired' error is returned to the user.
- separate script which runs at a fixed time each day disables invalid links 
- 'expires_at' is set to 24 hours after creation time.
- no support for disabling a URL. Only direct deletion supported. (Disabling can be achived by simply adding a 'status' column in the urls table)
- no per user profiles or auth. All DB is shared
