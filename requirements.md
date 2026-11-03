# Magus — Software Requirements Specification

| Document metadata | Value |
|---|---|
| Product name | Magus |
| Working product description | History revision platform |
| Document | Software Requirements Specification |
| Version | 0.1 |
| Status | Draft — pending completion of open decisions |
| Last updated | 2 November 2026 |
| Owner | [TO BE COMPLETED] |

> **Document status:** This is the initial requirements baseline for Magus. Confirmed decisions are recorded as requirements; unknown details are explicitly marked as open questions, assumptions or placeholders. A placeholder is not a confirmed product requirement.

## Table of Contents

1. [Document Overview](#1-document-overview)
2. [Product Overview](#2-product-overview)
3. [Product Scope](#3-product-scope)
4. [Users and Use Cases](#4-users-and-use-cases)
5. [Functional Requirements](#5-functional-requirements)
6. [Non-Functional Requirements](#6-non-functional-requirements)
7. [User Interface and User Experience](#7-user-interface-and-user-experience)
8. [Data Requirements](#8-data-requirements)
9. [External Interfaces and Integrations](#9-external-interfaces-and-integrations)
10. [Business and Technical Constraints](#10-business-and-technical-constraints)
11. [Error Handling and Edge Cases](#11-error-handling-and-edge-cases)
12. [Acceptance Criteria](#12-acceptance-criteria)
13. [Out of Scope](#13-out-of-scope)
14. [Assumptions, Dependencies and Open Questions](#14-assumptions-dependencies-and-open-questions)
15. [Requirements Traceability](#15-requirements-traceability)
16. [Future Considerations](#16-future-considerations)
17. [Change History](#17-change-history)

---

## 1. Document Overview

### 1.1 Purpose

This document defines the product requirements for Magus. It is intended to act as the primary reference for planning, implementing and verifying the initial release.

It describes the product's intended behaviour and quality requirements without unnecessarily prescribing its internal implementation. Technical decisions that have not yet been made are identified rather than assumed.

### 1.2 Scope of this document

This specification covers the initial MVP and records potential future functionality separately. It includes functional behaviour, user experience, content and data requirements, constraints, error handling and acceptance criteria.

### 1.3 Intended audience

- The project owner and developer.
- Future contributors or collaborators, if applicable.
- Anyone reviewing or testing the product.

### 1.4 Definitions and terminology

| Term | Definition |
|---|---|
| Magus | The software product described in this document. |
| MVP | Minimum Viable Product: the smallest independently usable release that delivers the product's core value. |
| Question bank | A collection of structured questions made available to Magus. |
| Question | A prompt presented to a user for an answer. |
| Multiple-choice question (MCQ) | A question with a set of selectable answer options. |
| Revision session | A sequence of questions answered during one use of the application. |
| Immediate feedback | Feedback presented after the user submits an answer, before moving to the next question. |
| [TERM] | [ADD DEFINITION] |

### 1.5 Requirement conventions

Requirements use unique identifiers and the following priority levels:

- **MUST:** Required for the MVP.
- **SHOULD:** Important, but not essential for the initial release.
- **COULD:** Desirable enhancement.
- **WON'T (this release):** Explicitly excluded from the current release.

The words **must**, **should** and **may** are used deliberately according to these priority levels. Each requirement should be verifiable. Where a decision is not yet known, the requirement is marked **TBD** or recorded in Section 14 rather than treated as settled.

### 1.6 Document status and ownership

- Document owner: [TO BE COMPLETED]
- Review date: [TO BE COMPLETED]
- Approval/status: [TO BE COMPLETED]

---

## 2. Product Overview

### 2.1 Product description

Magus is a web-based history revision platform. It presents students with multiple-choice history questions in a one-question-at-a-time format and provides immediate feedback after an answer is submitted.

The initial application is intended to use imported question banks rather than requiring question content to be authored directly within the application.

### 2.2 Problem addressed

**Problem statement:** [TO BE COMPLETED — describe the specific problem students experience with existing history revision methods and why Magus is being built.]

### 2.3 Intended users

The confirmed broad audience is students revising history.

Further audience details remain to be defined:

- Education level(s): [TO BE COMPLETED]
- Examination boards/specifications: [TO BE COMPLETED]
- Geographic market/curriculum: [TO BE COMPLETED]
- Any additional user groups: [TO BE COMPLETED]

### 2.4 Primary value proposition

Magus aims to provide a focused history revision experience centred on answering questions and receiving immediate feedback.

The specific benefits and differentiators to be validated are:

- [TO BE COMPLETED]
- [TO BE COMPLETED]
- [TO BE COMPLETED]

### 2.5 Central use cases

1. A student opens Magus.
2. The student accesses an available set of history questions.
3. The student answers a multiple-choice question.
4. Magus evaluates the submitted answer and presents feedback.
5. The student proceeds through further questions.

The exact topic-selection, session-start and session-completion flows are to be confirmed.

### 2.6 Product principles

The following principles guide the MVP:

- The question-answering experience is the central product experience.
- Questions are presented one at a time.
- Feedback is given immediately after submission.
- The initial question format is multiple choice.
- Question content is supplied through imported question banks.
- The initial release does not require user accounts.
- The application is a web application designed desktop-first, with mobile compatibility.

### 2.7 Differentiation

How Magus will distinguish itself from alternatives: [TO BE COMPLETED].

---

## 3. Product Scope

### 3.1 MVP scope

The MVP is focused on delivering a usable question-practice experience.

The following capabilities are confirmed as part of the intended MVP:

- A web application accessible without creating an account.
- Presentation of multiple-choice history questions.
- One question displayed at a time.
- Submission of an answer by the user.
- Immediate feedback after submission.
- Use of imported question banks.
- Desktop-first layout with mobile compatibility.

The exact behaviour and content of feedback, question-bank import process, session structure and progress display remain to be specified.

### 3.2 Post-MVP scope

Potential post-MVP functionality has not yet been committed.

Candidate features requiring future consideration include:

- Persistent user accounts and cross-device progress.
- Adaptive question selection.
- Spaced repetition.
- Daily revision targets.
- Detailed performance analytics.
- Additional question formats.
- Teacher or classroom functionality.
- AI-assisted question generation.

These are possibilities only. They are not MVP requirements.

### 3.3 Long-term product direction

[TO BE COMPLETED — describe the intended longer-term direction, if known.]

### 3.4 Scope control

A feature must not be added to the MVP solely because it may be useful in a later version. New functionality should be assessed against the core MVP objective: delivering a complete and reliable multiple-choice question-practice experience.

---

## 4. Users and Use Cases

### 4.1 User types

| User type | Description | Confirmed capabilities |
|---|---|---|
| Student / learner | A person using Magus to practise history questions. | Access and answer available questions. |
| Content administrator | [TO BE COMPLETED] | [TO BE COMPLETED] |
| Developer / project owner | Maintains the application and prepares/imports question content. | [TO BE COMPLETED] |

The initial release does not require student accounts. Whether a separate content-management role or interface is needed is undecided.

### 4.2 Use Case UC-001: Answer a multiple-choice question

- **Actor:** Student / learner.
- **Preconditions:**
  - The application is accessible.
  - At least one valid question is available to the application.
- **Trigger:** The student opens or starts a question-practice experience.
- **Main success flow:**
  1. Magus displays one multiple-choice question.
  2. Magus displays the available answer options.
  3. The student selects an answer.
  4. The student submits the selected answer.
  5. Magus evaluates the answer.
  6. Magus displays immediate feedback.
  7. The student can proceed according to the defined session flow.
- **Alternative flows:**
  - The student changes their selection before submission, if changing an answer is permitted. [DECISION REQUIRED]
  - The student selects a different question/topic, if that navigation is supported. [DECISION REQUIRED]
- **Failure scenarios:**
  - The question has missing or invalid answer data.
  - No questions are available.
  - The answer cannot be submitted because of an application error.
- **Expected outcome:** The student receives feedback for the submitted answer, or a clear recoverable error is presented.

### 4.3 Use Case UC-002: Access imported question content

- **Actor:** Application / developer or content administrator.
- **Preconditions:** A question bank has been prepared in an accepted format.
- **Trigger:** A question bank is made available to Magus.
- **Main success flow:** [TO BE COMPLETED — define how question banks are imported, validated and made available.]
- **Alternative flows:** [TO BE COMPLETED]
- **Failure scenarios:** [TO BE COMPLETED — e.g. invalid file, unsupported format, malformed question, duplicate content.]
- **Expected outcome:** Valid question content is available to the application; invalid content is rejected or reported in a defined way.

### 4.4 Use Case UC-003: Complete a revision session

- **Actor:** Student / learner.
- **Preconditions:** A session can be started and questions are available.
- **Trigger:** The student begins a revision session.
- **Main success flow:** [TO BE COMPLETED — define session length, question selection, progression and completion.]
- **Alternative flows:** [TO BE COMPLETED — e.g. leaving part-way through.]
- **Failure scenarios:** [TO BE COMPLETED]
- **Expected outcome:** [TO BE COMPLETED]

---

## 5. Functional Requirements

### 5.1 Question presentation

**FR-001: Display a question**

- **Description:** Magus must display a history question to the student.
- **Rationale:** Presenting questions is the central function of the product.
- **Preconditions:** A valid question is available.
- **Expected behaviour:** The application displays the question text and the answer options associated with it.
- **Acceptance criteria:**
  - Given a valid question is available, when the question is opened, then its question text and answer options are displayed.
  - Given no valid question is available, when the application attempts to display a question, then it presents a defined empty or unavailable state.
- **Priority:** MUST
- **Dependencies:** FR-010; DR-001.

**FR-002: Display one question at a time**

- **Description:** Magus must present no more than one active question at a time in the question-practice flow.
- **Rationale:** The confirmed interaction model is one question at a time.
- **Preconditions:** A question-practice flow is active.
- **Expected behaviour:** The current question is the sole active question requiring an answer.
- **Acceptance criteria:**
  - Given a question is active, when the student views the question screen, then only that question is presented as the active question.
- **Priority:** MUST
- **Dependencies:** FR-001.

**FR-003: Display multiple-choice options**

- **Description:** Magus must display the answer options associated with the current multiple-choice question.
- **Rationale:** Multiple choice is the confirmed initial question format.
- **Preconditions:** A valid multiple-choice question is available.
- **Expected behaviour:** Each answer option is presented as a selectable option and can be distinguished from the other options.
- **Acceptance criteria:**
  - Given a valid multiple-choice question, when it is displayed, then all of its configured answer options are available for selection.
- **Priority:** MUST
- **Dependencies:** FR-001; DR-001.

**FR-004: Allow an answer to be selected**

- **Description:** Magus must allow the student to select an answer option for the current question.
- **Rationale:** Students need to provide an answer.
- **Preconditions:** A question with valid answer options is displayed and is accepting input.
- **Expected behaviour:** The selected option is visibly distinguishable from unselected options.
- **Acceptance criteria:**
  - Given an unanswered question, when the student selects an option, then the interface visibly indicates which option is selected.
- **Priority:** MUST
- **Dependencies:** FR-003; UI-001.

**FR-005: Submit an answer**

- **Description:** Magus must allow the student to submit their selected answer.
- **Rationale:** Submission triggers answer evaluation and feedback.
- **Preconditions:** A question is active and the student has selected an answer.
- **Expected behaviour:** The application accepts the selected option for evaluation.
- **Acceptance criteria:**
  - Given an answer is selected, when the student activates the submission control, then the selected answer is submitted for evaluation.
  - Given no answer is selected, when the student attempts to submit, then the application follows the defined validation behaviour. [EXACT BEHAVIOUR TO CONFIRM]
- **Priority:** MUST
- **Dependencies:** FR-004; FR-006.

**FR-006: Evaluate a submitted answer**

- **Description:** Magus must determine whether a submitted answer matches the correct answer defined for the question.
- **Rationale:** Feedback depends on answer evaluation.
- **Preconditions:** A valid answer has been submitted and the question has a valid correct-answer reference.
- **Expected behaviour:** The application determines the answer result using the question's configured correct answer.
- **Acceptance criteria:**
  - Given the submitted option is the configured correct option, when the answer is evaluated, then the result is correct.
  - Given the submitted option is not the configured correct option, when the answer is evaluated, then the result is incorrect.
- **Priority:** MUST
- **Dependencies:** FR-005; DR-001.

**FR-007: Provide immediate feedback**

- **Description:** Magus must present feedback after a submitted answer has been evaluated and before the student proceeds to the next question.
- **Rationale:** Immediate feedback is part of the confirmed learning experience.
- **Preconditions:** An answer has been submitted and evaluated.
- **Expected behaviour:** The application communicates the outcome of the submitted answer in the current question flow.
- **Acceptance criteria:**
  - Given an answer has been evaluated, when the result is available, then feedback is displayed without requiring the student to navigate to another screen.
  - Given feedback is displayed, when the student has not yet proceeded, then the current question's result remains available to them.
- **Priority:** MUST
- **Dependencies:** FR-006; UI-002.

**FR-008: Distinguish correct and incorrect answers**

- **Description:** Magus must communicate whether the submitted answer was correct or incorrect.
- **Rationale:** Students must be able to understand the outcome of their attempt.
- **Preconditions:** An answer has been evaluated.
- **Expected behaviour:** The feedback state clearly identifies the result.
- **Acceptance criteria:**
  - Given a correct answer, when feedback is displayed, then the student can identify that the answer was correct.
  - Given an incorrect answer, when feedback is displayed, then the student can identify that the answer was incorrect.
- **Priority:** MUST
- **Dependencies:** FR-007.

**FR-009: Prevent unintended repeat submission**

- **Description:** Magus must prevent a single question attempt from being submitted repeatedly through accidental repeated activation of the submission control.
- **Rationale:** Repeated activation should not create ambiguous or duplicated answer attempts.
- **Preconditions:** An answer has already been accepted for the current question.
- **Expected behaviour:** The application treats the question as submitted and does not create additional attempts from repeated activation.
- **Acceptance criteria:**
  - Given an answer has been accepted, when the submission control is activated again for that same attempt, then no additional answer attempt is recorded or evaluated.
- **Priority:** MUST
- **Dependencies:** FR-005; FR-006.

### 5.2 Question-bank content

**FR-010: Make imported questions available**

- **Description:** Magus must be able to use question content supplied through imported question banks.
- **Rationale:** Imported question banks are the confirmed initial content source.
- **Preconditions:** A question bank has been supplied in a supported format.
- **Expected behaviour:** Valid imported questions can be made available to the question-practice experience.
- **Acceptance criteria:**
  - Given a valid question bank has been imported, when the application requests available questions, then its valid questions can be retrieved for presentation.
- **Priority:** MUST
- **Dependencies:** DR-001; INT-001.
- **Open detail:** Import format and import workflow are not yet defined.

**FR-011: Validate imported question content**

- **Description:** Magus must validate imported question content sufficiently to avoid presenting questions that lack required question or answer data.
- **Rationale:** Invalid content can prevent questions from being answered or evaluated reliably.
- **Preconditions:** A question bank is submitted for import or loading.
- **Expected behaviour:** Content that fails the agreed validation rules is not silently treated as a valid question.
- **Acceptance criteria:**
  - Given an imported question is missing a required field, when the content is validated, then the question is rejected or reported according to the defined import policy.
- **Priority:** MUST
- **Dependencies:** FR-010; DR-001.
- **Open detail:** Required fields and reporting behaviour are to be defined.

**FR-012: Associate questions with topics**

- **Description:** The question-content model should support associating a question with a topic or other content grouping.
- **Rationale:** Topic organisation may be required for students to access relevant revision content.
- **Preconditions:** The content structure defines topics or groupings.
- **Expected behaviour:** A question can be associated with its relevant topic or grouping.
- **Acceptance criteria:** [TO BE COMPLETED after the topic and curriculum model is decided.]
- **Priority:** SHOULD
- **Dependencies:** DR-002.
- **Open detail:** Whether topic selection is part of the MVP is not yet confirmed.

### 5.3 Session flow

**FR-013: Progress through questions**

- **Description:** Magus must provide a way for the student to proceed from a question after its feedback has been presented.
- **Rationale:** The confirmed experience involves answering questions sequentially.
- **Preconditions:** The current question has been answered and feedback has been displayed.
- **Expected behaviour:** The student can proceed according to the session's question sequence.
- **Acceptance criteria:**
  - Given feedback has been displayed, when the student chooses to continue, then the next available question is presented if one exists.
- **Priority:** MUST
- **Dependencies:** FR-007; FR-001.
- **Open detail:** The exact progression control and end-of-session behaviour are to be defined.

**FR-014: Indicate session progress**

- **Description:** Magus should communicate the student's position within a revision session if the session has a defined sequence or length.
- **Rationale:** A progress indicator may help students understand how far they have progressed.
- **Preconditions:** The session has a defined or calculable question sequence.
- **Expected behaviour:** The interface presents an accurate indication of progress.
- **Acceptance criteria:** [TO BE COMPLETED after session length and progress behaviour are decided.]
- **Priority:** SHOULD
- **Dependencies:** FR-013; UI-003.

**FR-015: Handle session completion**

- **Description:** Magus must provide a defined outcome when no further questions remain in the current session.
- **Rationale:** Students should not be left in an undefined state at the end of a question sequence.
- **Preconditions:** The current session has no further questions to present.
- **Expected behaviour:** [TO BE COMPLETED — define completion screen, summary and available next actions.]
- **Acceptance criteria:** [TO BE COMPLETED]
- **Priority:** MUST
- **Dependencies:** FR-013.
- **Open detail:** Session length and completion experience are undecided.

---

## 6. Non-Functional Requirements

Numerical performance, availability and compatibility targets have not yet been established. They must be agreed and tested rather than invented.

### 6.1 Usability

**NFR-001: Understandable question interaction**

- **Description:** The question, answer options, submission action and feedback must be distinguishable in the question interface.
- **Verification:** Usability review and interface testing.
- **Priority:** MUST

**NFR-002: Consistent interaction**

- **Description:** The interaction pattern for selecting, submitting and receiving feedback must remain consistent across supported questions.
- **Verification:** Interface review and functional testing.
- **Priority:** MUST

### 6.2 Performance

**NFR-003: Question presentation performance**

- **Description:** Question presentation and answer feedback must meet an agreed response-time target under the expected operating conditions.
- **Target:** [TO BE DEFINED]
- **Verification:** Performance testing.
- **Priority:** MUST

**NFR-004: Application responsiveness**

- **Description:** The application must remain responsive during normal question-practice use.
- **Target operating conditions:** [TO BE DEFINED]
- **Verification:** Performance and usability testing.
- **Priority:** MUST

### 6.3 Compatibility and responsiveness

**NFR-005: Desktop compatibility**

- **Description:** The application must support its intended desktop browser environment.
- **Supported browsers and minimum versions:** [TO BE DEFINED]
- **Verification:** Browser compatibility testing.
- **Priority:** MUST

**NFR-006: Mobile compatibility**

- **Description:** The web application must remain usable on supported mobile screen sizes.
- **Supported devices, screen widths and browsers:** [TO BE DEFINED]
- **Verification:** Responsive-layout and device testing.
- **Priority:** MUST

### 6.4 Accessibility

**NFR-007: Keyboard operation**

- **Description:** Core question interactions should be operable using a keyboard.
- **Verification:** Keyboard-only interaction testing.
- **Priority:** SHOULD

**NFR-008: Non-colour feedback**

- **Description:** Correct and incorrect feedback must not rely on colour alone to communicate the result.
- **Verification:** Accessibility review.
- **Priority:** MUST

**NFR-009: Readable content**

- **Description:** Question text and answer options must remain legible at supported viewport sizes.
- **Verification:** Responsive and accessibility review.
- **Priority:** MUST

### 6.5 Reliability and data integrity

**NFR-010: Reliable answer evaluation**

- **Description:** Given the same valid question and submitted option, answer evaluation must produce the same result.
- **Verification:** Automated tests using known correct and incorrect answers.
- **Priority:** MUST

**NFR-011: Valid question content**

- **Description:** The application must not present imported content as a valid question if it lacks the fields required for display and evaluation.
- **Verification:** Import validation tests.
- **Priority:** MUST

### 6.6 Security and privacy

**NFR-012: No required student account**

- **Description:** A student must be able to access the initial question-practice experience without creating an account or signing in.
- **Verification:** End-to-end test of a new visitor accessing and answering questions.
- **Priority:** MUST

**NFR-013: Data minimisation**

- **Description:** The MVP should not collect personal student information unless it is necessary for a confirmed MVP function.
- **Verification:** Review of data collection and network behaviour.
- **Priority:** MUST

### 6.7 Maintainability

**NFR-014: Separation of question content and interface**

- **Description:** Question-bank content should be maintained separately from the interface presentation logic.
- **Rationale:** The product uses imported question banks and should allow content to be updated without rewriting question-screen presentation.
- **Verification:** Code and content-structure review.
- **Priority:** MUST

**NFR-015: Extensible question structure**

- **Description:** The question representation should allow the content model to evolve without requiring unrelated interface functionality to be rewritten.
- **Verification:** Architecture and code review.
- **Priority:** SHOULD

---

## 7. User Interface and User Experience Requirements

### 7.1 Platform and layout

**UI-001: Web application**

- Magus must be delivered as a web application.
- The initial layout priority is desktop.
- The application must also support mobile use.
- Exact supported viewport widths and browser targets: [TO BE DEFINED].

### 7.2 Question screen

**UI-002: Question presentation**

The question screen must provide distinct areas for:

- The current question text.
- The available answer options.
- The answer-submission action.
- Feedback after submission.

Exact layout, navigation and visual hierarchy: [TO BE DEFINED].

### 7.3 Feedback state

**UI-003: Answer feedback state**

After submission, the interface must visibly communicate whether the answer was correct or incorrect. Feedback must be available before the student proceeds.

The following details remain open:

- Whether the correct option is highlighted after an incorrect answer: [TO BE COMPLETED]
- Whether an explanation is displayed: [TO BE COMPLETED]
- Whether feedback includes a sound, animation or other effect: [TO BE COMPLETED]
- How the student proceeds to the next question: [TO BE COMPLETED]

### 7.4 Visual identity

The intended visual identity has not yet been specified.

- Brand name: Magus (working name).
- Product descriptor: [TO BE COMPLETED; e.g. Magus Revision].
- Colour palette: [TO BE COMPLETED].
- Typography: [TO BE COMPLETED].
- Logo/icon: [TO BE COMPLETED].
- Light/dark theme: [TO BE COMPLETED].
- Motion and animation principles: [TO BE COMPLETED].

### 7.5 Interface states

The design must account for the following states:

| State | Required behaviour |
|---|---|
| Loading | [DEFINE loading presentation] |
| Question available | Display the current question and its options. |
| Option selected | Visually distinguish the selected option. |
| Answer submitted | Prevent unintended repeat submission and evaluate the answer. |
| Correct answer | Display clear correct-answer feedback. |
| Incorrect answer | Display clear incorrect-answer feedback. |
| No questions available | [DEFINE empty state] |
| Invalid question content | Do not present the invalid question as answerable; [DEFINE user-facing message]. |
| Session complete | [DEFINE completion state] |
| Application error | [DEFINE recoverable error state] |

---

## 8. Data Requirements

### 8.1 Data overview

The MVP requires structured question content to be supplied through imported question banks.

The precise import format and storage mechanism have not been selected. This section defines the conceptual data needs without prescribing a database schema.

### 8.2 Core data entities

**DR-001: Question**

A question must contain sufficient information for Magus to present it and evaluate a multiple-choice response.

Proposed conceptual attributes:

| Attribute | Status | Description |
|---|---|---|
| Question identifier | Required in principle; format TBD | Distinguishes the question from other questions. |
| Question text | Required | The prompt presented to the student. |
| Answer options | Required | The selectable options for the question. |
| Correct answer reference | Required | Identifies the correct option. |
| Explanation | Optional / undecided | Additional explanation shown after answering. |
| Topic | Undecided | Topic or grouping associated with the question. |
| Difficulty | Undecided | Optional difficulty classification. |
| Curriculum/specification | Undecided | Examination board or specification association. |
| Source/attribution | Undecided | Origin or attribution information, where needed. |

**DR-002: Topic or content grouping**

Whether topics are required in the MVP, and how they are represented, remains undecided.

Potential attributes:

- Topic identifier: [TO BE DEFINED]
- Topic name: [TO BE DEFINED]
- Parent topic/group: [TO BE DEFINED]
- Curriculum/specification: [TO BE DEFINED]

**DR-003: Question bank**

The application must be able to use a collection of imported questions. The bank's metadata, versioning, file format and validation rules remain to be defined.

### 8.3 Data validation

At minimum, a question intended for presentation must have:

- Question text.
- A valid set of answer options.
- A reference to a correct answer that corresponds to one of those options.

Further rules to define:

- Minimum and maximum number of answer options: [TO BE DEFINED]
- Whether duplicate options are permitted: [TO BE DEFINED]
- Whether question text may contain rich text, images or other media: [TO BE DEFINED]
- Whether explanations are optional or mandatory: [TO BE DEFINED]
- Handling of duplicate question identifiers: [TO BE DEFINED]
- Character encoding and supported content: [TO BE DEFINED]

### 8.4 Persistence and session data

The initial release does not require student accounts.

The following are undecided:

- Whether session progress is held only during the current browser session.
- Whether session progress survives a page refresh.
- Whether anonymous progress is stored locally.
- Whether any performance data is retained after a session.
- Whether question responses are stored at all.

No persistent student profile or cross-device progress should be assumed.

### 8.5 Import and export

- Import format(s): [TO BE DEFINED]
- Import method: [TO BE DEFINED]
- Import validation/reporting: [TO BE DEFINED]
- Whether content can be exported: [TO BE DEFINED]
- Question-bank versioning/update behaviour: [TO BE DEFINED]

---

## 9. External Interfaces and Integrations

### 9.1 Confirmed interfaces

- A web browser is the user-facing interface.
- Question-bank content must be supplied to Magus through an import mechanism.

### 9.2 External services

No external service or third-party integration has been confirmed.

Potential services, if any: [TO BE COMPLETED].

### 9.3 Import interface

**INT-001: Question-bank input**

- **Description:** Magus must accept question-bank content through the import mechanism selected for the MVP.
- **Format:** [TO BE DEFINED]
- **Method:** [TO BE DEFINED]
- **Validation response:** [TO BE DEFINED]
- **Failure behaviour:** Invalid or unsupported content must not silently become available as valid question content.
- **Priority:** MUST

### 9.4 Authentication

Student authentication is not required for the initial release. Whether any separate authentication is needed for content management or deployment is undecided.

---

## 10. Business and Technical Constraints

### 10.1 Confirmed product constraints

| ID | Constraint | Status |
|---|---|---|
| CON-001 | The initial product is a web application. | Confirmed |
| CON-002 | The interface is desktop-first and must be mobile-compatible. | Confirmed |
| CON-003 | The initial question format is multiple choice. | Confirmed |
| CON-004 | Questions are presented one at a time. | Confirmed |
| CON-005 | Feedback is provided immediately after answer submission. | Confirmed |
| CON-006 | The initial content source is imported question banks. | Confirmed |
| CON-007 | Student accounts are not required initially. | Confirmed |

### 10.2 Development constraints

- Development resources: [TO BE COMPLETED]
- Budget: [TO BE COMPLETED]
- Target MVP date: [TO BE COMPLETED]
- Hosting/deployment constraints: [TO BE COMPLETED]
- Required technology stack: [TO BE COMPLETED]
- Licensing constraints: [TO BE COMPLETED]

### 10.3 Technical decisions not yet established

The following must not be treated as settled:

- Front-end framework: [TO BE COMPLETED]
- Back-end architecture: [TO BE COMPLETED]
- Data storage approach: [TO BE COMPLETED]
- Question-bank file format: [TO BE COMPLETED]
- Hosting provider: [TO BE COMPLETED]
- Build and deployment process: [TO BE COMPLETED]
- Testing framework: [TO BE COMPLETED]

---

## 11. Error Handling and Edge Cases

The application must define predictable behaviour for abnormal conditions. The cases below identify required areas; exact messages and recovery flows remain to be designed.

### 11.1 Question content

| ID | Condition | Required behaviour |
|---|---|---|
| EH-001 | No questions are available. | Do not display a broken or empty question; show a defined unavailable state. |
| EH-002 | Question text is missing. | Do not present the record as a valid question. |
| EH-003 | Answer options are missing or invalid. | Do not allow the question to be answered. |
| EH-004 | Correct-answer reference does not match an available option. | Do not evaluate the question as valid; report or exclude it according to the import policy. |
| EH-005 | Imported content contains an unsupported format. | Reject or report the unsupported content; do not silently misinterpret it. |

### 11.2 Answer submission

| ID | Condition | Required behaviour |
|---|---|---|
| EH-006 | Student attempts to submit without selecting an option. | Do not evaluate an absent answer; present the defined validation response. |
| EH-007 | Student activates submit repeatedly. | Do not create duplicate submissions for the same question attempt. |
| EH-008 | Student attempts to change an answer after submission. | Follow the answer-locking policy once defined. |
| EH-009 | An evaluation error occurs. | Do not display a potentially incorrect result as authoritative; show a recoverable error state. |

### 11.3 Session flow

| ID | Condition | Required behaviour |
|---|---|---|
| EH-010 | The student reaches the end of the available questions. | Present the defined session-completion state. |
| EH-011 | The student refreshes or closes the page mid-session. | Follow the session-persistence policy once defined. |
| EH-012 | A question becomes unavailable during a session. | Do not leave the student trapped on an unanswerable question; provide a defined recovery path. |

### 11.4 General application failures

- Unexpected application error: [DEFINE error presentation and recovery].
- Browser loses connectivity: [DEFINE expected behaviour, if relevant to the chosen architecture].
- Question-bank loading fails: [DEFINE retry or fallback behaviour].
- Imported bank is partially invalid: [DEFINE whether valid questions can still be imported].

---

## 12. Acceptance Criteria

### 12.1 Core question experience

The following conditions must be met for the core question experience to be accepted:

- [ ] A user can open Magus without creating an account.
- [ ] A valid imported multiple-choice question can be displayed.
- [ ] Only one question is active at a time.
- [ ] The question's answer options are displayed.
- [ ] A user can select an answer option.
- [ ] The selected option is visibly distinguishable.
- [ ] A user can submit the selected answer.
- [ ] The system correctly identifies a configured correct answer.
- [ ] The system correctly identifies a configured incorrect answer.
- [ ] Immediate feedback is displayed after evaluation.
- [ ] Correct and incorrect outcomes are distinguishable without relying on colour alone.
- [ ] The user can proceed through the defined question sequence.
- [ ] The application handles the absence of available questions without presenting a broken interface.

### 12.2 Content acceptance

- [ ] The agreed question-bank format is documented.
- [ ] A valid question bank can be imported or loaded using the agreed process.
- [ ] Required question fields are validated.
- [ ] Invalid questions are not presented as valid, answerable questions.
- [ ] Correct-answer references are validated against the available options.

### 12.3 Platform acceptance

- [ ] The application works in the agreed desktop browser support range.
- [ ] The question-answering experience is usable at the agreed mobile viewport sizes.
- [ ] Core interactions can be completed using the supported input methods.
- [ ] The interface presents defined loading, feedback, empty and error states.

### 12.4 System-level acceptance

- [ ] All MVP MUST requirements have been implemented or explicitly dispositioned.
- [ ] Each implemented requirement has a verification method.
- [ ] Core question and answer-evaluation tests pass.
- [ ] Invalid question data tests pass.
- [ ] No known critical defect prevents a student from completing the core question flow.
- [ ] The MVP scope has not silently expanded to include deferred features.

---

## 13. Out of Scope

The following are not part of the confirmed initial release:

| Feature | Scope decision |
|---|---|
| Student accounts and sign-in | Not required for the initial release. |
| AI-generated questions | Not included in the confirmed initial content approach. |
| Non-multiple-choice question formats | Not included in the initial question format. |
| Native mobile applications | Not part of the confirmed web-app scope. |
| Social features and leaderboards | Not established as MVP functionality. |
| Subscription and payment systems | Not established as MVP functionality. |
| Teacher/classroom management | Not established as MVP functionality. |
| Advanced analytics | Not established as MVP functionality. |
| Adaptive revision and spaced repetition | Potential future work; not an MVP commitment. |

This section may be revised if the project owner explicitly changes the MVP scope.

---

## 14. Assumptions, Dependencies and Open Questions

### 14.1 Assumptions

These are provisional and must be confirmed or rejected.

| ID | Assumption | Status |
|---|---|---|
| A-001 | Question banks will contain structured data that can be validated before questions are presented. | To confirm |
| A-002 | A question can be evaluated by comparing the selected option with a correct-answer reference in its question data. | To confirm |
| A-003 | The initial student experience can operate without a persistent student identity. | Consistent with confirmed no-account decision; persistence details remain open. |
| A-004 | The first release will be developed and maintained by the project owner. | To confirm |

### 14.2 Dependencies

| ID | Dependency | Status |
|---|---|---|
| DEP-001 | A valid source of history question-bank content. | Required; source and rights/permissions to be confirmed. |
| DEP-002 | An agreed question-bank structure and import method. | Not yet defined. |
| DEP-003 | A supported web deployment environment. | Not yet selected. |
| DEP-004 | A defined set of target browsers and mobile viewport sizes. | Not yet defined. |

### 14.3 Open questions 

#### Product and curriculum

1. Which curriculum or examination specifications will Magus support initially?  
   **Answer:** AQA GCSE History 

2. Which education levels are in scope for the first release?  
   **Answer:** Year 7, Year 8, Year 9, Year 10, Year 11

3. Is the initial content focused on specific historical periods/topics, or is it intended to be broad?  
   **Answer:** Restricted to curriculum listed topics. Year 7 to Core Year 9 is taken from school curriculum ; Year 10 and Year 11 is taken from AQA Specification

4. What specific problem should Magus solve better than existing revision products?  
   **Answer:** Short-form revision that can be completed digitally and quickly, ideally while completing mundane low-focus tasks such as commuting.

#### Question experience

5. How many answer options should a multiple-choice question normally contain?  
   **Answer:** 10 ; Or how many the teacher sets for a homework

6. Can students change their selected option before submitting?  
   **Answer:** Yes

7. Can students change or appeal an answer after submission?  
   **Answer:** Yes- They should be able to submit a request for their teacher to review, with a small text box to explain why they have appealed.

8. Should feedback show only whether the answer is correct, or also reveal the correct answer and an explanation?  
   **Answer:** A brief explanation should be displayed in a pop up box, regardless of if the answer was correct or incorrect.

9. Should a question explanation be required in the question bank or optional?  
   **Answer:** It should be required

10. How does a student start a session: choose a topic, start a general practice session, or use another method?  
    **Answer:** Choose a topic for independent study ; Or complete set topic by teacher.

11. How long should a session be, or how is its end determined?  
    **Answer:** It endures for the length of the questions

12. What should happen when a session ends?  
    **Answer:** They return to topic screen

#### Content and imports

13. What format should question banks use (e.g. JSON, CSV or another format)?  
    **Answer:** JSON

14. How are question banks imported: bundled with the application, loaded from files by the developer, or uploaded through an interface?  
    **Answer:** Loaded from a pre-built JSON

15. Who creates and maintains the question banks?  
    **Answer:** Developer. 

16. What is the source of the question content, and what permissions or licensing apply?  
    **Answer:** Taken from AQA Guidance

17. Should questions be organised by topic, period, examination board, specification, difficulty or another classification?  
    **Answer:** Per year, per topic

#### Progress and persistence

18. Should the application show a question counter or progress indicator during a session?  
    **Answer:** Both

19. Should a session's results be shown at the end?  
    **Answer:** Yes

20. Should progress survive a browser refresh or closing the page?  
    **Answer:** Not in MVP

21. If there are no accounts, should any anonymous progress be stored locally?  
    **Answer:** There will be rudimentary account services

#### Design and platform

22. What visual direction should Magus use?  
    **Answer:** modern SaaS Design

23. Is a light theme, dark theme or both required?  
    **Answer:** Both

24. Which desktop browsers and minimum versions should be supported?  
    **Answer:** Chrome, Edge, Firefox, Safari

25. What minimum mobile viewport should remain usable?  
    **Answer:** 320px

#### Technical and delivery

26. Which technology stack, if any, has already been selected?  
    **Answer:** The MVP will be web-based with HTML, CSS and JS

27. Where will the application be hosted?  
    **Answer:** First on Github, then any appropriate domain hosting site.

28. Is there a target date or budget for the MVP?  
    **Answer:** Target date for MVP Completion is the 1st of December. No standard or fixed budget. Development should favour free/open source tools and services wherever possible

29. Are there any additional constraints, preferences or non-negotiable design decisions?  
    **Answer:** N/A frn

---

## 15. Requirements Traceability

The following matrix links each current requirement to its principal use case and verification route. Test-case identifiers can be added when the test suite is established.

| Requirement | Use case | Verification |
|---|---|---|
| FR-001 | UC-001 | Test that valid question text and options display. |
| FR-002 | UC-001 | Test that only one question is active at a time. |
| FR-003 | UC-001 | Test that all configured options display. |
| FR-004 | UC-001 | Test option selection and visible selected state. |
| FR-005 | UC-001 | Test answer submission and empty-selection validation. |
| FR-006 | UC-001 | Test correct and incorrect answer evaluation. |
| FR-007 | UC-001 | Test feedback appears after evaluation. |
| FR-008 | UC-001 | Test correct and incorrect feedback states. |
| FR-009 | UC-001 | Test repeated submission is not duplicated. |
| FR-010 | UC-002 | Test valid question-bank content becomes available. |
| FR-011 | UC-002 | Test invalid question data is rejected or reported. |
| FR-012 | UC-001 / UC-002 | Test question-topic association once defined. |
| FR-013 | UC-003 | Test progression to the next question. |
| FR-014 | UC-003 | Test progress indication once session rules are defined. |
| FR-015 | UC-003 | Test the defined end-of-session behaviour. |

### 15.1 Traceability maintenance

When requirements are added, changed or removed:

- Keep identifiers stable where the underlying requirement remains the same.
- Assign a new identifier to a genuinely new requirement.
- Update affected use cases and acceptance criteria.
- Add or update the corresponding verification route.
- Record material changes in the change history.

---

## 16. Future Considerations

The following ideas may be considered after the MVP has been delivered and evaluated. They are not current requirements.

- Accounts and persistent learner profiles.
- Revision history across sessions and devices.
- Adaptive question selection based on previous performance.
- Spaced-repetition scheduling.
- Daily question targets.
- Topic-level mastery and performance analytics.
- Additional question formats.
- AI-assisted question creation or explanation.
- Teacher, class or institution features.
- Gamification, streaks and achievements.
- Additional subjects beyond history.

Any future feature must be assessed separately for user value, implementation cost, data requirements and effect on the existing product.

---

## 17. Change History

| Version | Date | Changes |
|1|02/11/2026|1|
| 0.1 | 2 November 2026 | Initial draft based on confirmed product decisions.|

---

**End of document**
