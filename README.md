# HappenHere
![HappenHere in different viewports](static/images/README/hh_air.png)
Image from: [Am I Resoponsive](https://ui.dev/amiresponsive)

## Contents:
- [Description](#description)
- [Design and Planning](#design-and-planning)
    - [Design & Ideation](#design-and-ideation)
    - [Wireframes](#wireframes)
    - [Database](#database)
    - [Agile Methodology](#agile-methodology)
    - [Technologies Used](#technologies-used)    
- [Features](#features)
- [Testing and Validation](#testing-and-validation)
- [Bugs](#bugs)
- [Future features and Development](#future-features-and-development)
- [AI](#ai)
- [Deployment](#deployment)
- [Credits](#credits)

## Description
HappenHere is a community event booking platform, where users can host, browse and join local happenings.

## Design and Planning


### Design and Ideation

#### Typography
![HappenHere fonts - Raleway and Roboto](static/images/README/hh_typography.png)
#### Colour Scheme
![HappenHere colour scheme](static/images/README/happenhere_colour_scheme.png)

### Wireframes
| Page | Wireframe |
| --- | ----------- |
| Home | <img src="static/images/README/wireframes/hh_wireframe_Homepage.png" alt="HappenHere Wireframe Home" width="70%"> |
| All Events | <img src="static/images/README/wireframes/hh_wireframe_All_Events.png" alt="HappenHere Wireframe All Events" width="70%"> |
| Event Detail | <img src="static/images/README/wireframes/hh_wireframe_Event_Detail.png" alt="HappenHere Wireframe Event Detail" width="70%"> |
| Event Detail - Edit | <img src="static/images/README/wireframes/hh_wireframe_Event_Detail_Edit.png" alt="HappenHere Wireframe Event Detail Edit" width="70%"> |
| Event Detail - Cancel booking / Delete event | <img src="static/images/README/wireframes/hh_wireframe_Event Detail_Cancel Booking_Delete.png" alt="HappenHere Wireframe Event Detail - Cancel / Book" width="70%"> |
| My Events - Host | <img src="static/images/README/wireframes/hh_wireframe_My_Events_Host.png" alt="HappenHere Wireframe My Events Host" width="70%"> |
| My Events - Host Form | <img src="static/images/README/wireframes/hh_wireframe_My Events_Host_Form.png" alt="HappenHere Wireframe My Events Fost Form" width="70%"> |
| My Events - Booked / Published | <img src="static/images/README/wireframes/hh_wireframe_My Events_Booked_Past.png" alt="HappenHere Wireframe My Events Booked / Past" width="70%"> |

### Database
![HappenHere Database ERC](static/images/README/hh_database_erd.png)

### Agile Methodology

- must-have
- should-have
- could-have

#### Project Board & User Stories
| Detail | Image |
| --- | ----------- |
| Issues in repo (leftover) | <img src="static/images/README/hh_issues_userstories.png" alt="HappenHere Issues - User Stories" width="70%"> |
| Github Project Board & User Stories | <img src="static/images/README/hh_project_board.png" alt="HappenHere Project Board - User Stories" width="70%"> |

The project board for this project can be seen here:
<a href="https://github.com/users/KoroYsabela/projects/8" target="_blank">HappenHere - Project Board</a>

### Technologies Used




## Features
| Feature | Image |
| --- | ----------- |
| Homepage  | Image |
| All Events | Image |
| Event Detail - Book | Image |
| Event Detail - Cancel Booking | Image |
| Event Detail - Edit Event | Image |
| Event Detail - Delete Event | Image |
| My Events - Host Tab | Image |
| My Events - Host Event Form | Image |
| My Events - Booked Tab | Image |
| My Events - Past Tab | Image |

### User Authentication

### Custom Model & CRUD Functionality



## Testing and Validation
Everything in the table was tested, but due to high number of files only a few images were taken and included.
### HTML
| HTML | Pass/Fail |
| --- | ----------- |
| `events/templates/events/index.html`  | <img src="static/images/README/hh_home_index_html_validation.png" alt="HappenHere index.html validation pass" width="70%"> |
| `events/templates/events/all_events.html` | PASS |
| `events/templates/events/event_detail.html` | WARNING & ERRORS (if using link to an event) - due to the use of django summernote widgets / PASS (when using `.html` file with warnings from the use of django code) |
| `myevents/templates/myevents/my_events.html` | PASS |
| `myevents/templates/myevents/login.html` | PASS |
| `myevents/templates/myevents/logout.html` | PASS |
| `myevents/templates/myevents/signup.html` | PASS |

### Python
| HTML | Pass/Fail |
| --- | ----------- |
| `config/settings.py`  | <img src="static/images/README/hh_python_linter.png" alt="HappenHere python linter" width="70%"> |
| `config/urls.py` | PASS |
| `events/admin.py` | PASS |
| `events/forms.py` | PASS |
| `events/models.py` | PASS |
| `events/urls.py` | PASS |
| `events/views.py` | PASS |
| `myevents/forms.py` | PASS |
| `myevents/models.py` | PASS |
| `myevents/urls.py` | PASS |
| `myevents/views.py` | PASS |

### JavaScript
| CSS | Pass/Fail |
| --- | ----------- |
| `static/js/evensHome.js` | <img src="static/images/README/hh_eventsHome_jshint.png" alt="HappenHere eventsHome.js jshint validation" width="70%"> |

### CSS
| CSS | Pass/Fail |
| --- | ----------- |
| `static/css/style.css` | <img src="static/images/README/hh_css_validation.png" alt="HappenHere css validation pass" width="70%"> |

### Google's Lighthouse Performance
| Device | Performance | Accessibility | Best Practices | SEO |
| --- | ----------- | ----------- | ----------- | ----------- |
| Mobile | ... | ... | ... | ... |
| Desktop | ... | ... | ... | ... |

Performance is slightly lower due to having images for the event cards. Although a max size limit was added to do how much clouadinary could handle, in addition to the compressed default image, a lot of images on a page will naturally cause performance issues.

Best Practices were also lower due HTTPS from allowing the user to upload their own image.

### WAVE Accessibility
General testing on different pages using this tool showed no errors:

<img src="static/images/README/hh_wave_accessibility.png" alt="HappenHere wave accessibility tool" width="60%">

### Browser Compatability


## Bugs


## Future features and Development


## AI


## Deployment

View the deployed project on heroku: <a href="https://happenhere-ea5273c6b3f0.herokuapp.com/" target="_blank">HappenHere</a>

## Credits