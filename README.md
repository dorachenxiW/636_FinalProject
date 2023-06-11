# 636_FinalProject

# NZ Winter Olympics Project Report
## Routes and Functions
As per requirement, this project has two interfaces. The public interface is accessible by the default route / and the admin interface is accessed by route /admin. The two interfaces are seperate and have no interaction for safety consideration. The two routes returns two seperate HTML templates, base.html and adminbase.html and there are different templates that extends from either interfaces seperately and respectively.

For the public access, this interface has two major functions, the List Event function and the List Team Member function. The List Event function uses route /listevents, and gets data about the events from the "events" table in the database, passes it into the template eventlist.html and the templates display it as a table of list. The List Team Member function has the same mechanism in displaying a table of members: the route /listmembers gets data from the database and passes into the template memberlist.html, but in addition, the memberlist.html template is set to have another route /listmembers/athlete/detail, by clicking the member's name, in order to bring up a specific member's events or results details into another HTML page. A hidden form is used to pass the member ID into the route /listmembers/athlete/details, using POST methods, in order to pick up the right member. Depending on if the picked member has the required data in the database, this route returns to either the template athlete.html or athlete_nocurrentinfo.html. The graph below shows different routes and templates and how data flows.

```mermaid
graph TD;
   
    /-->B[LIST EVENT FUNCTION]-->C[Route /listevents];
    C[Route /listevent]-->|GET|D(eventlist.html);
    /-->E[LIST TEAM MEMBER FUNCTION]-->F[Route /listmembers];
    F[Route /listmembers]-->|GET|G(memberlist.html)-->|POST|H[Route /listmembers/athlete/detail];
    H[Route /listmembers/athlete/detail]-->|GET|I(athlete.html)
    H[Route /listmembers/athlete/detail]-->|GET|J(athlete_nocurrentinfo.html)
```

The admin interface has five main functions and each function has one or many templates which are extended from the adminbase.html. 

The Search funtion is accessed by route /search and returns to template search.html, which sets two routes, route /admin/search/result_member and route /admin/search/result_event. Both routes get data through the form in template search.html and pass it back to the same template. 

The Add/Edit Member function uses route /admin/addeditmember which returns to template addeditmember.html. This html then uses route /admin/member/add to get data from the user and passes it to database, then redirects to route /admin/addeditmember to show the member being added in the template addeditmember.html. To edit the member, the route /admin/member/edit/<memberid> gets the member ID and then gets the matching data from the databae then passes it into another template editmember.html. This new template page then gets data input from user and updates them in the database then redirect to route /admin/addeditmember to go back to template addeditmember.html.
   
The Add Events and Event Stages function has a base route /admin/addeventsandstages and it gets data from database back to template addevents.html. Similarly as the Add Member Function, addevents.html uses route /admin/event/add to get data from the user and passes it back to the database then redirects to route /admin/addeventsandstages. To add an stage event, the route /admin/eventstage/add/<eventid> gets the event ID from user then gets the matching data from the database then passes into either addeventstage_nocurrentstage.html or addeventstages.html, depending on if the chosen event has any current eventstage. The both templates work the same way, which get data from users, using the same route /admin/eventstage/add, and pass it back to database. This route also gets data from the updated database again then return to template addeventstage.html.
   

```mermaid
graph TD;

/admin-->B[SEARCH FUNCTION]-->C[Route /search]-->|GET|D(search.html);
D(search.html)-->|POST|E[Route /admin/search/result_member]-->D(search.html)
D(search.html)-->|POST|F[Route /admin/search/result_event]-->D(search.html)

/admin-->G[Add/Edit FUNCTION]-->H[Route /admin/addeditmember]-->|GET|I(addeditmember.html)
I(addeditmember.html)-->|POST|J[Route /admin/member/add]-->H[Route /admin/addeditmember]-->I(addeditmember.html)
I(addeditmember.html)-->K[Route /admin/member/edit/<memberid>]-->|GET|L(editmember.html)-->|POST|M[Route /admin/updatemember]-->H[Route /admin/addeditmember]-->I(addeditmember.html)
   
/admin-->N[ADD EVENT AND EVENT STAGES]-->O[Route /admin/addeventsandstages]-->P(addevents.html)-->Q[Route /admin/event/add]-->O[Route /admin/addeventsandstages]-->P(addevents.html) 
P(addevents.html)-->S[Route /admin/eventstage/add/<eventid>]-->T[addeventstage.html]-->U[Route /admin/eventstage/add]-->T[addeventstage.html]
S[Route /admin/eventstage/add/<eventid>]-->V[addeventstage_nocurrentstage.html]-->U[Route /admin/eventstage/add]-->T[addeventstage.html]
```   
The Addscore or Position function uses route /admin/addscore, and gets data from the database to template addscores_event.html. This page then gets data from the user by route /admin/addscores/event to be used to get more data from the database, then passes them to either addscores_noeventstage.html or addscores_eventstage.html. The template addscores_eventstage.html then uses route /admin/addscores/stageid to get data from database then pass them into addsocres_update.html. The last page then gets data from user and put it back into the database using route /admin/addscores/update then returns to templates addscore_display.html.

The Report function has route /admin/reports and it returns to template report.html. This template then is set to have route /admin/report/type and it gets data from the user and passes it into the either reports_medal.html or reports_member.html. Route /admin/report/type also gets data from the database and passes them into either templates.     
```mermaid
graph TD;

/admin-->B[Route /admin/addscore]-->C(addscores_event.html)-->D[Route /admin/addscores/event]-->E(addscores.noeventstage.html)
D[Route /admin/addscores/event]-->F(addscores_eventstage.html)-->G[Route /admin/addscores/stageid]-->H(addscore_update.html)-->I[Route /admin/addscores/update]-->J(addscore_display.html)   
   
/admin-->k[Route /admin/reports]-->L(report.html)-->M[Route /admin/report/type]-->N(reports_medal.html)   
M[Route /admin/report/type]-->O(reports_member.html)  
```   




## Assumptions
- The listmembers function from the public interface, the list showing has changed its order. Instead of showing memberID and TeamID, "Name" is created to combine FirstName and LastName from the db so the clickable link doesnt have a confusion. Also because of the link, the names have been moved to the first colunm.  
- Add/Edit function has a assumption that the memberid is readyonly and not chaangeable when editting. Also, a drop down has created to choose a team as I assume there is only new team added at the same time as adding a member. 

## Changes
### Database Changes
### App Changes

test
Change to show getting to PA




