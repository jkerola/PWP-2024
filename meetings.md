# Meetings notes

## Meeting 1.

- **DATE: 7th February 2024**
- **ASSISTANTS: Ivan Sanchez Milara**

### Minutes

Duration of the meeting was 30 minutes. The agenda of the meeting was to receive feedback for deliverable 1 - project plan. Several improvement points were suggested by the course staff. Based on the feedback the project plan focuses too much on technical concepts, while it should have focused more on explaining the underlying concept instead. Some parts that were too technical can be moved into deliverable 2. Another point that came up was that at some points the explanations provided should be expanded upon, or the explanation was not relevant to what was requested in the section.

### Action points

**Group information**

- List all group members on the table

**DL1. RESTTful API description**

RESTful API description

- Focuses too much on technicalities. Focus more into motivating the API and explain it a bit more in detail. ✅
- Wrong terminology. Avoid terms like login or public link that are more referred to applications. Authentication instead of registered users. ✅ (recheck this)
- Architecture not needed in this section. ✅

Main concepts and relations

- Make a new graph. Take example from lecture 2 slides - Forum Resource hierarchy.
- Old graph can be moved into deliverable 2.
- Focuses too much on technical concepts. **Focus should be on the main concepts and relations**. Explanation should be altered to be something similar to the second paragraph of this section (To create a poll...).
- Improve wording at places. Remove words like "database" etc.

API uses

- Must add external service.
- Auxiliary service - check Lovelace

Related work

- Explain strawpoll better.
- Add example of a client, for example frontend.

Update resources allocation if information is incorrect.

## Meeting 2.

- **DATE: 21st February 2024**
- **ASSISTANTS: Ivan Sanchez Milara**

### Minutes

Duration of the meeting was 25 minutes. The agenda of the meeting was to receive feedback for deliverable 2 - database design and implementation. At the start of the meeting we discussed about what tools will be utilized in the implementation. The application will be implemented using Python, while the client will be running on Node. The ORM being used is Prisma. PostgreSQL is used for the database, but assistant alternatively recommended using SQLite instead, as it can be easier to set up. The feedback from assistant was overall positive, and only a few changes were suggested.

### Action points

Database design

- `Role Enumeration` can be moved into `User model`.
- Improve `Restrictions` column's REGEX and make sure `schema.prisma` matches it.

Resources allocation

- Update Resources allocation table if information is not correct.

## Meeting 3.

- **DATE: 25th March 2024**
- **ASSISTANTS: Ivan Sanchez Milara**

### Minutes

Meeting lasted around 40 minutes. Point of the meeting was to recieve feedback for deliverable 3 - API Implementation. We did not have time to test the functionality of our API implementation during the meeting. Other than this, we recieved feedback on what we should improve for the final delivery. The main issues that came up during the meeting were: low test coverage, wiki/documentation needs more explanation for addressability and authentication. 

### Action points

- Check that implementation works in the next meeting

Wiki report
  - Provide explanations for why the system is addressable
  - Explain why PATCH is used instead of PUT
  - Explain how authentication was implemented to ensure that the system is stateless. How to get the keys and when keys are used?

Basic implementation
- Add references for code that was taken from exercises
- Explain converters in more detail
- PollItems and Polls have low test coverage. Especially error situations (409, 404, 400...) are not tested.
- Update instructions on how to run the API and tests.



## Meeting 4.

- **DATE: 10th April 2024**
- **ASSISTANTS: Mika Oja**

### Minutes

Duration of the meeting was 20 minutes. Point of the meeting was to recieve feedback for deliverable 4 - API documentation and hypermedia. We had some issues that need addressing: all GET requests are missing responses, some error codes are missing (415), state diagram needs to be reworked. 

### Action points

Documentation
- Missing examples from all GET requests, so need to add these
- Certain response codes are missing, such as 415. These need to be added

Hypermedia design
- Current diagram is not a state diagram. This needs to be reworked.

## Midterm meeting

- **DATE:**
- **ASSISTANTS:**

### Minutes

_Summary of what was discussed during the meeting_

### Action points

_List here the actions points discussed with assistants_

## Final meeting

- **DATE:**
- **ASSISTANTS:**

### Minutes

_Summary of what was discussed during the meeting_

### Action points

_List here the actions points discussed with assistants_
