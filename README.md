# AI CODING AGENT PROMPT — EXACT CLINIC ADMIN DASHBOARD RECREATION USING PYTHON DJANGO ONLY.

## ROLE

You are an expert **UI/UX designer, frontend engineer, and DJANGO full-stack web developer**.

Your task is to develop a **professional Clinic Management Admin Dashboard using DJANGO** that visually matches the supplied reference image **as closely and accurately as possible**. Start by creating the first APP.

The reference image represents the desired dashboard appearance for a clinic website.

**IMPORTANT:**
Do NOT create the promotional flyer surrounding the dashboard.
Do NOT place the dashboard inside a flyer.
Do NOT use the reference image as a background image.

Instead, build the dashboard as a **real, functional web interface using HTML/CSS/JavaScript and the project's existing technology stack**.

The final result should look like the dashboard shown in the reference image, while being a real responsive application.

---

# 1. PRIMARY OBJECTIVE

Recreate the following clinic dashboard:

**Clinic Name:** CareWell Clinic
**Dashboard User:** Admin
**Role:** Administrator

The dashboard should have:

* Dark left navigation sidebar
* Top navigation/header
* Welcome message
* Date selector
* Notification icon
* Admin profile/avatar
* Four statistics cards
* Appointments overview line chart
* Appointments status doughnut chart
* Recent appointments section
* Top services section
* Monthly revenue bar chart
* Clean white cards
* Rounded corners
* Subtle shadows
* Green clinic/medical branding
* Blue, purple, orange and red chart/status colors
* Professional healthcare SaaS appearance
* Responsive mobile-first behavior

The implementation must be a **real dashboard**, not a static screenshot.

---

# 2. REFERENCE DESIGN

Use the supplied reference image as the **primary visual authority**.

When there is a conflict between generic design conventions and the reference image, prioritize the reference image.

The design should feel like:

> Modern + Professional + Medical + Secure + Clean + Premium + Easy to Manage

Do not introduce unrelated visual styles.

Avoid:

* Excessive gradients
* Glassmorphism
* Neon colors
* Excessive animations
* Huge empty spaces
* Cartoon-style medical graphics
* Overly colorful backgrounds
* Unnecessary UI elements
* Different sidebar structures
* Different dashboard card layouts

---

# 3. OVERALL PAGE STRUCTURE

Create the dashboard using this structure:

```text
┌──────────────────────────────────────────────────────────────┐
│                       TOP HEADER                             │
├───────────────┬──────────────────────────────────────────────┤
│               │                                              │
│               │             DASHBOARD CONTENT                │
│               │                                              │
│   SIDEBAR     │  Welcome Header                              │
│               │                                              │
│               │  Statistics Cards                            │
│               │                                              │
│               │  Appointment Chart     Status Chart          │
│               │                                              │
│               │  Recent Appointments  Top Services           │
│               │                                              │
│               │  Monthly Revenue Chart                       │
│               │                                              │
└───────────────┴──────────────────────────────────────────────┘
```

Desktop layout:

* Fixed/structured left sidebar
* Main content occupies remaining width
* Content has generous but controlled spacing
* Dashboard should fit naturally inside a 1440px–1920px desktop viewport

---

# 4. COLOR PALETTE

Use colors very close to the reference.

## Primary Green

Use clinic green as the main brand color:

```css
--primary-green: #22C55E;
--primary-green-dark: #16A34A;
--primary-green-light: #DCFCE7;
```

Use green for:

* Branding
* Positive statistics
* Active states where appropriate
* Buttons
* Growth indicators
* Selected navigation elements
* Chart highlights
* Section labels

## Sidebar

Use a dark navy/charcoal sidebar:

```css
--sidebar-bg: #101D32;
--sidebar-bg-dark: #0B1628;
--sidebar-text: #FFFFFF;
--sidebar-muted: #B8C2D1;
```

## Main Background

```css
--page-background: #F5F7FA;
```

## Cards

```css
--card-background: #FFFFFF;
--border-color: #E5E7EB;
```

## Chart Colors

Use:

```css
Blue:   #2563EB
Green:  #22C55E
Purple: #8B5CF6
Orange: #F59E0B
Red:    #EF4444
```

Do not randomly introduce additional brand colors.

---

# 5. TYPOGRAPHY

Use a modern sans-serif font.

Preferred:

```text
Inter
```

Fallback:

```text
system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif
```

Typography hierarchy:

### Main dashboard title

Large, bold, dark text.

### Welcome text

Medium-sized dark text.

### Card labels

Small-to-medium gray text.

### Main numerical values

Large, bold, dark text.

### Supporting information

Small gray text.

### Positive growth indicators

Green.

Typography must be clean and highly readable.

---

# 6. LEFT SIDEBAR

Create a dark vertical sidebar matching the reference.

Desktop width should approximately be:

```text
280px–320px
```

The sidebar should occupy the full viewport height.

Use:

```text
CareWell Clinic
```

at the top.

Include a medical/clinic logo icon beside the clinic name.

---

# 7. SIDEBAR NAVIGATION

The sidebar must contain these navigation items in this exact order:

1. Dashboard
2. Appointments
3. Patients
4. Doctors
5. Services
6. Prescriptions
7. Billing
8. Payments
9. Reports
10. Messages
11. Settings

Each navigation item should have:

* Icon
* Text label
* Hover state
* Active state

---

## ACTIVE DASHBOARD ITEM

The Dashboard navigation item must be visually highlighted.

Reference appearance:

* Blue background
* Rounded corners
* White icon
* White text

Example:

```text
┌───────────────────────────┐
│ 🏠  Dashboard             │
└───────────────────────────┘
```

The active state should be clearly visible.

---

# 8. SIDEBAR ICONS

Use a professional icon library if available in the project.

Recommended:

* Lucide
* Heroicons
* Font Awesome

Do NOT use random emojis as interface icons.

Recommended icon mapping:

```text
Dashboard      → Home
Appointments   → Calendar
Patients       → Users
Doctors        → User/Doctor icon
Services       → Network/Services icon
Prescriptions  → Clipboard/Medical icon
Billing        → Receipt
Payments       → Credit Card
Reports        → File/Chart
Messages       → Mail
Settings       → Settings
```

Icons should be approximately:

```text
18px–22px
```

---

# 9. SIDEBAR ADMIN PROFILE

At the bottom of the sidebar, create an administrator profile area.

Reference:

```text
[Profile Photo]

Admin
Administrator
●
```

The profile section should include:

* Circular profile image/avatar
* Name: `Admin`
* Role: `Administrator`
* Small green online indicator

The profile area should remain at the bottom of the sidebar.

---

# 10. TOP HEADER

The main content should have a top header.

On desktop, show:

### Left side

A hamburger/menu icon where appropriate.

### Main welcome message

```text
Welcome back, Admin 👋
```

Below it:

```text
Here's what's happening with your clinic today.
```

The welcome text should be positioned near the upper-left of the content area.

---

# 11. HEADER RIGHT SIDE

On the right side of the header include:

### Date selector

Display:

```text
May 13, 2025
```

with a calendar icon.

The date component should look like a modern white rounded input/control.

### Notification

Add a bell icon.

Show a small notification indicator.

### Admin avatar

Show a small circular profile image/avatar.

---

# 12. DASHBOARD STATISTICS CARDS

Immediately below the header, create **four statistics cards**.

They must appear in a 4-column layout on desktop.

Responsive behavior:

```text
Desktop:
4 columns

Tablet:
2 columns

Mobile:
1 column
```

Each card should have:

* Small icon
* Label
* Large number
* Supporting text
* Growth indicator

Cards should have:

* White background
* Rounded corners
* Thin/light border
* Very subtle shadow
* Comfortable padding

---

# 13. CARD 1 — TOTAL APPOINTMENTS

Display:

```text
Total Appointments

42

Today

↑ 12% from yesterday
```

Use a blue calendar/appointment icon.

The number:

```text
42
```

must be prominent.

The growth indicator should be green.

---

# 14. CARD 2 — PATIENTS

Display:

```text
Patients

580

Total

↑ 8% this month
```

Use a green users/patients icon.

Number:

```text
580
```

---

# 15. CARD 3 — DOCTORS

Display:

```text
Doctors

12

Active

↑ 2 new this month
```

Use a purple doctor/user icon.

Number:

```text
12
```

---

# 16. CARD 4 — REVENUE

Display:

```text
Revenue

KES 125,600

This Month

↑ 15% from last month
```

Use an orange revenue/finance icon.

The currency must be:

```text
KES
```

because this is intended for the Kenyan market.

---

# 17. APPOINTMENTS OVERVIEW SECTION

Below the statistics cards, create a large chart card.

Title:

```text
Appointments Overview
```

Add a small period dropdown on the right:

```text
Today ▼
```

The chart should resemble the reference.

---

# 18. APPOINTMENTS LINE CHART

Create a professional line chart.

Use two datasets:

```text
Today
Yesterday
```

Today should be represented by a strong blue line.

Yesterday should be represented by a lighter/dashed gray line.

X-axis:

```text
8AM
10AM
12PM
2PM
4PM
6PM
```

Y-axis should represent appointment count.

Approximate Today data:

```javascript
[
  0,
  8,
  14,
  9,
  11,
  5,
  3,
  0
]
```

Approximate Yesterday data:

```javascript
[
  0,
  3,
  2,
  6,
  4,
  5,
  2,
  3
]
```

The exact data can be adjusted slightly if necessary, but the visual shape should closely resemble the reference.

Use:

* Smooth line
* Small points
* Light grid lines
* Clean axes
* No unnecessary chart decorations
* Responsive sizing

---

# 19. APPOINTMENTS BY STATUS

Beside the appointment overview chart on desktop, create another large card.

Title:

```text
Appointments by Status
```

Create a doughnut chart.

Center of doughnut:

```text
42
Total
```

Statuses:

```text
Confirmed   22 (52%)
Completed   12 (29%)
Pending      6 (14%)
Cancelled    2 (5%)
```

Use these colors:

```text
Confirmed → Blue
Completed → Green
Pending   → Orange
Cancelled → Red
```

The legend should appear to the right of the chart on desktop.

On smaller screens, position the legend below the chart.

---

# 20. MAIN CONTENT GRID

Desktop layout for this section:

```text
Appointments Overview      Appointments by Status
        60%                         40%
```

Or approximately:

```text
2fr 1.35fr
```

The exact proportions should visually resemble the reference.

---

# 21. RECENT APPOINTMENTS CARD

Create a white card titled:

```text
Recent Appointments
```

Display the following appointments:

### Appointment 1

```text
John Otieno
09:00 AM
General Checkup
Confirmed
```

### Appointment 2

```text
Mary Akinyi
10:00 AM
Dental Consultation
Completed
```

### Appointment 3

```text
Peter Mwangi
11:00 AM
Follow Up
Pending
```

### Appointment 4

```text
Grace Wanjiku
02:00 PM
Antenatal Care
Confirmed
```

Each row should contain:

* Patient avatar/icon
* Patient name
* Appointment time
* Service
* Status badge

---

# 22. STATUS BADGES

Create professional rounded status badges.

### Confirmed

Green text/background.

### Completed

Green or slightly different success treatment.

### Pending

Orange text/background.

### Cancelled

Red text/background.

The badge should be compact.

Example:

```text
[ Confirmed ]
```

Do not use huge badges.

---

# 23. VIEW ALL APPOINTMENTS

At the bottom of the Recent Appointments card add:

```text
View all appointments →
```

Use green/blue accent styling consistent with the reference.

This should be clickable.

---

# 24. TOP SERVICES CARD

Create a white card titled:

```text
Top Services
```

List:

```text
General Checkup        18
Dental Care             9
Antenatal Care          7
Laboratory Test         5
Child Health            3
```

Each row should have:

* Service name
* Count

At bottom:

```text
View all services →
```

---

# 25. LOWER CONTENT GRID

The lower section should visually resemble:

```text
Recent Appointments | Top Services | Monthly Revenue
```

On desktop:

```text
Approximately 45% | 25% | 30%
```

The exact width can be adjusted to maintain a clean layout.

---

# 26. MONTHLY REVENUE CARD

Create a white card titled:

```text
Monthly Revenue
```

Show:

```text
KES 125,600
↑ 15% from last month
```

Then create a vertical bar chart.

Months:

```text
Jan
Feb
Mar
Apr
May
```

Approximate values:

```text
Jan → 85,000
Feb → 100,000
Mar → 102,000
Apr → 120,000
May → 125,600
```

The final May bar should be highlighted in clinic green.

The other bars should use a soft blue/light blue tone.

Chart should have:

* Clean grid
* Minimal axes
* No unnecessary borders
* Responsive dimensions

---

# 27. CARD DESIGN

Every dashboard card should follow a consistent design system.

Use approximately:

```css
border-radius: 12px;
background: #ffffff;
border: 1px solid #e5e7eb;
box-shadow: 0 2px 8px rgba(0,0,0,0.04);
```

Do not make the shadows too strong.

Cards should feel:

* Clean
* Modern
* Premium
* Professional
* Medical/SaaS

---

# 28. DASHBOARD SPACING

Pay very close attention to spacing.

Use a consistent spacing system.

Recommended:

```text
4px
8px
12px
16px
20px
24px
32px
```

Main dashboard padding:

```text
24px–32px desktop
16px mobile
```

Card gaps:

```text
16px–24px
```

Do not allow components to touch each other.

---

# 29. RESPONSIVE DESIGN

The dashboard MUST be fully responsive.

## Desktop

At approximately:

```text
≥ 1200px
```

Show:

* Full sidebar
* Four statistic cards
* Two-column chart section
* Three-column lower section

---

## Tablet

At approximately:

```text
768px–1199px
```

Use:

* Collapsible/sidebar navigation
* Two statistic cards per row
* Charts stacked or two-column where appropriate
* Lower cards adapted to available width

---

## Mobile

At approximately:

```text
< 768px
```

The interface must become mobile-friendly.

Use:

* Collapsible sidebar/drawer
* Hamburger menu
* One statistic card per row
* Charts stacked vertically
* Cards full width
* Horizontally scrollable tables/lists where necessary
* Proper touch targets
* No horizontal page overflow

The dashboard must still look polished on a phone.

---

# 30. MOBILE SIDEBAR

On mobile:

* Hide the full sidebar by default.
* Show hamburger menu.
* Clicking hamburger opens sidebar/drawer.
* Clicking outside the drawer closes it.
* Add smooth but subtle transition.
* Do not allow the drawer to break the page.

---

# 31. HEADER RESPONSIVENESS

On mobile:

* Keep hamburger/menu button visible.
* Simplify the welcome section.
* Keep notification and profile controls accessible.
* Date selector may become compact.
* Do not allow header elements to overlap.

---

# 32. CHART TECHNOLOGY

Use a reliable chart library compatible with the project's stack.

Preferred options:

### If React

Use:

```text
Recharts
```

or

```text
Chart.js
```

### If Django templates

Use:

```text
Chart.js
```

### If another framework is already configured

Use the project's existing chart solution where practical.

Do NOT introduce a completely unnecessary framework just for the charts.

Charts must be real interactive charts rather than static images.

---

# 33. FUNCTIONAL INTERACTIONS

The dashboard should not merely look correct.

Implement functional UI behavior.

At minimum:

### Sidebar

* Navigation items clickable
* Active navigation state
* Mobile drawer

### Date selector

* Should open a date-selection UI or work as a date input.

### Period selector

The:

```text
Today ▼
```

dropdown should work.

Possible options:

```text
Today
This Week
This Month
This Year
```

### Notifications

Bell icon should be clickable.

### Profile

Admin profile should be clickable.

### Dashboard links

```text
View all appointments
View all services
```

should be functional navigation links.

---

# 34. DATA ARCHITECTURE

Do NOT hard-code the UI in a way that makes it impossible to connect to a backend later.

Separate dashboard data from presentation.

Create a clean data structure such as:

```javascript
dashboardStats
appointments
appointmentStatus
topServices
monthlyRevenue
```

For example:

```javascript
dashboardStats = {
    totalAppointments: 42,
    patients: 580,
    doctors: 12,
    revenue: 125600
}
```

This will allow the dashboard to later consume real database data.

---

# 35. IF THIS IS A DJANGO PROJECT

If the existing project is Django:

**DO NOT replace Django with another backend framework.**

Use:

* Django views
* Django templates where appropriate
* Django static files
* Django models for real data
* Django URL routing
* Chart.js for charts

The dashboard should be structured so that sample values can later be replaced with Django query results.

If Django REST Framework is already installed and used by the project, you may expose dashboard data through APIs where appropriate.

---

# 36. IF THIS IS A REACT PROJECT

If the existing project is React:

Use reusable components.

Recommended structure:

```text
Dashboard
├── Sidebar
├── Header
├── StatsCards
│   ├── TotalAppointmentsCard
│   ├── PatientsCard
│   ├── DoctorsCard
│   └── RevenueCard
├── AppointmentsOverview
├── AppointmentStatusChart
├── RecentAppointments
├── TopServices
└── MonthlyRevenue
```

Do not create one massive component containing the entire dashboard.

---

# 37. COMPONENT REUSABILITY

Build reusable components for:

* Cards
* Navigation items
* Status badges
* Chart containers
* Appointment rows
* Service rows
* Buttons
* Dropdowns

Avoid duplicated markup wherever possible.

---

# 38. ACCESSIBILITY

The dashboard should be accessible.

Implement:

* Semantic HTML
* Proper button elements
* Accessible navigation
* ARIA labels where necessary
* Keyboard navigation
* Visible focus states
* Good color contrast
* Alt text for images
* Accessible chart descriptions where practical

Do not sacrifice the visual design.

---

# 39. PERFORMANCE

Keep the dashboard fast.

Avoid:

* Huge image assets
* Unnecessary dependencies
* Excessive JavaScript
* Repeated API calls
* Unoptimized rendering
* Heavy animations

Charts should load efficiently.

---

# 40. ANIMATIONS

Use subtle animations only.

Examples:

* Sidebar opening
* Card hover
* Dropdown opening
* Button hover
* Chart appearance

Animation duration:

```text
150ms–250ms
```

Avoid flashy animations.

---

# 41. EXACT VISUAL PRIORITIES

When comparing your implementation against the reference image, prioritize these elements in this order:

### Priority 1

Overall dashboard structure.

### Priority 2

Sidebar size, color and navigation positioning.

### Priority 3

Header positioning.

### Priority 4

Statistics card arrangement.

### Priority 5

Charts and their proportions.

### Priority 6

Lower dashboard cards.

### Priority 7

Typography.

### Priority 8

Spacing.

### Priority 9

Colors.

### Priority 10

Icons and small visual details.

The final dashboard should immediately look like the same product shown in the reference.

---

# 42. DO NOT RECREATE THE PROMOTIONAL FLYER

The uploaded image contains promotional material around the dashboard, including:

* UniqueTechCamp branding
* "PROFESSIONAL CLINIC WEBSITE"
* Marketing slogans
* Contact information
* Key features strip
* Promotional CTA

IGNORE those elements.

They are NOT part of the dashboard application.

Only recreate the **actual clinic dashboard UI** visible in the central device/interface.

---

# 43. IMPORTANT: DO NOT USE THE SCREENSHOT AS THE UI

Do NOT simply:

```html
<img src="dashboard-screenshot.png">
```

That is NOT acceptable.

The dashboard must be recreated using:

```text
HTML
CSS
JavaScript
Components
Charts
Icons
Real UI elements
```

The screenshot may only be used as a visual reference.

---

# 44. BRANDING

For the initial demo data, use:

```text
CareWell Clinic
```

Use a simple medical/clinic logo.

However, structure the branding so that it can easily be changed later to another clinic's:

* Name
* Logo
* Contact information
* Colors

Do not hard-code the brand in dozens of unrelated places.

---

# 45. SAMPLE DASHBOARD DATA

Use the following initial sample data.

## Statistics

```text
Total Appointments: 42
Patients: 580
Doctors: 12
Revenue: KES 125,600
```

## Appointment statuses

```text
Confirmed: 22
Completed: 12
Pending: 6
Cancelled: 2
Total: 42
```

## Recent appointments

```text
John Otieno — 09:00 AM — General Checkup — Confirmed

Mary Akinyi — 10:00 AM — Dental Consultation — Completed

Peter Mwangi — 11:00 AM — Follow Up — Pending

Grace Wanjiku — 02:00 PM — Antenatal Care — Confirmed
```

## Top services

```text
General Checkup — 18
Dental Care — 9
Antenatal Care — 7
Laboratory Test — 5
Child Health — 3
```

## Revenue

```text
Jan — KES 85,000
Feb — KES 100,000
Mar — KES 102,000
Apr — KES 120,000
May — KES 125,600
```

---

# 46. CODE QUALITY

Write production-quality code.

Requirements:

* Clean folder structure
* Reusable components
* Meaningful variable names
* No unnecessary duplication
* No inline styles unless genuinely necessary
* No massive CSS file containing unrelated rules
* No unused dependencies
* No console errors
* No broken links
* No broken images
* No layout overflow

---

# 47. BEFORE CODING

First inspect the existing project.

Determine:

1. Framework
2. Existing frontend structure
3. Existing CSS system
4. Existing component architecture
5. Existing authentication
6. Existing routing
7. Existing database models
8. Existing static/media configuration
9. Existing design system
10. Existing dependencies

**DO NOT destroy or rewrite an existing working application unnecessarily.**

Reuse the project's existing architecture where possible.

---

# 48. IMPLEMENTATION STRATEGY

Work in the following order:

### Step 1

Inspect the entire relevant project structure.

### Step 2

Identify the correct dashboard entry point.

### Step 3

Create the dashboard layout.

### Step 4

Implement the sidebar.

### Step 5

Implement the header.

### Step 6

Implement statistics cards.

### Step 7

Implement appointments overview chart.

### Step 8

Implement appointment status doughnut chart.

### Step 9

Implement recent appointments.

### Step 10

Implement top services.

### Step 11

Implement monthly revenue chart.

### Step 12

Implement responsive behavior.

### Step 13

Add interactions.

### Step 14

Test desktop.

### Step 15

Test tablet.

### Step 16

Test mobile.

### Step 17

Fix all visual inconsistencies.

---

# 49. VISUAL QA REQUIREMENT

After implementation, inspect the dashboard visually.

Compare it against the reference image.

Check:

* Sidebar width
* Sidebar color
* Navigation spacing
* Header height
* Card sizes
* Card spacing
* Chart proportions
* Typography
* Icon sizes
* Border radius
* Shadows
* Alignment
* White space
* Responsive behavior

If anything looks substantially different from the reference, correct it.

Do not stop after the first implementation.

---

# 50. FINAL ACCEPTANCE CRITERIA

The implementation is complete only when:

* [ ] Dashboard closely matches the reference image
* [ ] Sidebar matches the reference structure
* [ ] Sidebar uses dark navy styling
* [ ] Dashboard active item is highlighted
* [ ] Admin profile appears at sidebar bottom
* [ ] Header matches the reference structure
* [ ] Four statistics cards are present
* [ ] Statistics values match the provided sample
* [ ] Appointments line chart works
* [ ] Appointment status doughnut chart works
* [ ] Recent appointments section works
* [ ] Top services section works
* [ ] Monthly revenue chart works
* [ ] KES currency is used
* [ ] Icons are professional
* [ ] Cards have consistent styling
* [ ] Responsive desktop layout works
* [ ] Responsive tablet layout works
* [ ] Responsive mobile layout works
* [ ] Mobile sidebar works
* [ ] Dropdowns/interactions work
* [ ] No horizontal overflow
* [ ] No console errors
* [ ] No broken routes
* [ ] No broken assets
* [ ] Code is clean and maintainable
* [ ] Dashboard is built as real UI, NOT as an image
* [ ] Promotional flyer elements are NOT included in the dashboard

---

# 51. MOST IMPORTANT INSTRUCTION

The supplied image is the **visual reference**.

Your goal is not to create something that is merely "similar to a clinic dashboard."

Your goal is to reproduce the **same visual composition and user experience**:

```text
Dark sidebar
        ↓
Clinic branding
        ↓
Navigation
        ↓
Admin profile

Main area
        ↓
Welcome header
        ↓
Date + notifications + profile
        ↓
4 statistic cards
        ↓
Appointments Overview + Status Chart
        ↓
Recent Appointments + Top Services + Revenue
```

Match the reference as closely as possible while keeping the implementation:

* Functional
* Responsive
* Reusable
* Maintainable
* Backend-ready
* Professional
* Production-quality

**Start by inspecting the existing project before making changes. Then implement the dashboard incrementally and verify each section visually before moving to the next.**
