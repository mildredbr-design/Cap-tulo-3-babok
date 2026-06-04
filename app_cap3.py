# -*- coding: utf-8 -*-
"""
Simulador CBAP - BABOK v3
Chapter 3: Business Analysis Planning and Monitoring
250 preguntas (en inglés, como el examen real CBAP)
"""

import streamlit as st
import random

st.set_page_config(page_title="CBAP Simulator - Chapter 3", page_icon="📘", layout="centered")

# ------------------------------------------------------------------
# THEME: dark navy / gold  ·  Playfair Display + Source Sans 3
# ------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@300;400;600&display=swap');

.stApp {
    background-color: #0a1428;
    color: #e8e6e1;
}
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #d4af37 !important;
}
p, span, label, div, .stMarkdown {
    font-family: 'Source Sans 3', sans-serif !important;
}
.titulo {
    font-family: 'Playfair Display', serif;
    font-size: 2.1rem;
    color: #d4af37;
    text-align: center;
    margin-bottom: 0.2rem;
}
.subtitulo {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 1rem;
    color: #9fb3c8;
    text-align: center;
    margin-bottom: 1.5rem;
    font-weight: 300;
}
.tarea-tag {
    display: inline-block;
    background-color: #1c2c4c;
    color: #d4af37;
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-bottom: 12px;
    border: 1px solid #d4af37;
}
.stButton>button {
    background-color: #d4af37;
    color: #0a1428;
    font-weight: 600;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1.5rem;
}
.stButton>button:hover {
    background-color: #e8c860;
    color: #0a1428;
}
.correcto {
    background-color: #143820;
    border-left: 4px solid #2e7d32;
    padding: 12px;
    border-radius: 6px;
    margin-top: 10px;
}
.incorrecto {
    background-color: #3a1414;
    border-left: 4px solid #c62828;
    padding: 12px;
    border-radius: 6px;
    margin-top: 10px;
}
.explicacion {
    background-color: #11203c;
    border-left: 4px solid #d4af37;
    padding: 12px;
    border-radius: 6px;
    margin-top: 10px;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

# ==================================================================
# BANCO DE PREGUNTAS - 250
# Campos: pregunta, opciones (4), respuesta (string exacto), explicacion, tarea
# ==================================================================

PREGUNTAS = [

    # ============================================================
    # 3.1 PLAN BUSINESS ANALYSIS APPROACH  (Q1-Q50)
    # ============================================================
    {
        "pregunta": "What is the primary purpose of the Plan Business Analysis Approach task?",
        "opciones": [
            "To define an appropriate method to conduct business analysis activities",
            "To elicit requirements from stakeholders",
            "To approve the final solution scope",
            "To manage stakeholder conflicts during a project"
        ],
        "respuesta": "To define an appropriate method to conduct business analysis activities",
        "explicacion": "Plan Business Analysis Approach defines an appropriate method to conduct business analysis activities, including the activities themselves, timing, techniques, deliverables, and how they will be performed.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which of the following is the primary output of the Plan Business Analysis Approach task?",
        "opciones": [
            "Business Analysis Approach",
            "Stakeholder Engagement Approach",
            "Governance Approach",
            "Information Management Approach"
        ],
        "respuesta": "Business Analysis Approach",
        "explicacion": "The single output of Plan Business Analysis Approach is the Business Analysis Approach, which identifies the methodology, activities, deliverables, and timing of the business analysis work.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "What is the only input to the Plan Business Analysis Approach task?",
        "opciones": [
            "Needs",
            "Business Analysis Approach",
            "Requirements",
            "Designs"
        ],
        "respuesta": "Needs",
        "explicacion": "Needs is the only input. The way the business analyst approaches the work is shaped by the problem or opportunity being addressed.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which two general categories describe most business analysis planning approaches?",
        "opciones": [
            "Predictive and adaptive",
            "Formal and informal",
            "Linear and iterative",
            "Centralized and decentralized"
        ],
        "respuesta": "Predictive and adaptive",
        "explicacion": "BABOK describes planning approaches as ranging across a spectrum from predictive (minimizing uncertainty, formal deliverables) to adaptive (rapid delivery of value in short iterations).",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "A predictive approach to business analysis is most appropriate when:",
        "opciones": [
            "Uncertainty must be minimized and risk of an incorrect solution is high",
            "Requirements emerge rapidly and value must be delivered in short iterations",
            "Stakeholders prefer minimal documentation",
            "The team works exclusively in two-week sprints"
        ],
        "respuesta": "Uncertainty must be minimized and risk of an incorrect solution is high",
        "explicacion": "Predictive approaches focus on minimizing upfront uncertainty and ensuring the solution is fully defined before implementation begins, which is useful when risk or cost of error is high.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "An adaptive approach to business analysis focuses primarily on:",
        "opciones": [
            "Rapid delivery of business value in short iterations",
            "Producing complete documentation before development",
            "Eliminating all change requests",
            "Centralized sign-off of all requirements upfront"
        ],
        "respuesta": "Rapid delivery of business value in short iterations",
        "explicacion": "Adaptive approaches accept greater uncertainty in exchange for delivering value quickly through iterative cycles, refining requirements as the work progresses.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which of the following is an element of the Plan Business Analysis Approach task?",
        "opciones": [
            "Formality and Level of Detail of Business Analysis Deliverables",
            "Stakeholder Communication Needs",
            "Change Control Process",
            "Plan Traceability Approach"
        ],
        "respuesta": "Formality and Level of Detail of Business Analysis Deliverables",
        "explicacion": "Elements of this task include Planning Approach, Formality and Level of Detail of Business Analysis Deliverables, Business Analysis Activities, Timing of Business Analysis Work, Complexity and Risk, and Acceptance.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "In a predictive approach, business analysis deliverables typically are:",
        "opciones": [
            "Formal and detailed",
            "Informal and high-level",
            "Verbal and undocumented",
            "Optional"
        ],
        "respuesta": "Formal and detailed",
        "explicacion": "Predictive approaches usually call for formal, detailed deliverables, whereas adaptive approaches favor lighter, less formal documentation.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which factor would most likely increase the formality and level of detail of business analysis deliverables?",
        "opciones": [
            "A highly regulated environment with compliance requirements",
            "A small, co-located team building an internal prototype",
            "A short, low-risk initiative",
            "A team that meets daily to discuss requirements verbally"
        ],
        "respuesta": "A highly regulated environment with compliance requirements",
        "explicacion": "Regulatory and compliance contexts typically demand greater formality and detail in deliverables for traceability and auditability.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "The 'Timing of Business Analysis Work' element addresses:",
        "opciones": [
            "When business analysis tasks will be performed and how they relate to other activities",
            "How requirements will be stored and accessed",
            "Who has authority to approve requirements",
            "Which metrics will measure performance"
        ],
        "respuesta": "When business analysis tasks will be performed and how they relate to other activities",
        "explicacion": "Timing concerns when the activities should be performed, whether some are repeated, and how they integrate with the overall initiative schedule.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "The 'Acceptance' element of the Plan Business Analysis Approach task refers to:",
        "opciones": [
            "Determining how the business analysis approach will be agreed upon and approved",
            "Accepting the final solution into production",
            "Stakeholders accepting requirements changes",
            "Acceptance testing of the delivered software"
        ],
        "respuesta": "Determining how the business analysis approach will be agreed upon and approved",
        "explicacion": "Acceptance addresses how the chosen approach is reviewed and agreed to by key stakeholders, and any decision-making or change processes affecting the approach itself.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which technique is commonly used to estimate the effort required for business analysis activities when planning the approach?",
        "opciones": [
            "Estimation",
            "Data Mining",
            "Prototyping",
            "Acceptance and Evaluation Criteria"
        ],
        "respuesta": "Estimation",
        "explicacion": "Estimation is used to forecast the effort, time, and cost of business analysis work and to determine an appropriate approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "A business analyst reviews documentation from a previous similar project to help shape the planned approach. Which technique is being used?",
        "opciones": [
            "Document Analysis",
            "Observation",
            "Data Modelling",
            "Survey or Questionnaire"
        ],
        "respuesta": "Document Analysis",
        "explicacion": "Document Analysis examines existing documentation (including from past initiatives) to inform decisions, including how to plan the current approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which technique helps the business analyst decompose the planned work into smaller, more manageable components when defining the approach?",
        "opciones": [
            "Functional Decomposition",
            "Mind Mapping",
            "Glossary",
            "Data Dictionary"
        ],
        "respuesta": "Functional Decomposition",
        "explicacion": "Functional Decomposition breaks down the planned business analysis work and deliverables into smaller parts, aiding estimation and organization of the approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which stakeholder is responsible for managing the project and is concerned about how the business analysis approach affects the schedule?",
        "opciones": [
            "Project Manager",
            "Regulator",
            "Domain Subject Matter Expert",
            "Sponsor"
        ],
        "respuesta": "Project Manager",
        "explicacion": "The Project Manager ensures the business analysis approach is compatible with other project activities and the overall plan, and so is a key stakeholder.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "A government body imposes rules that constrain the chosen business analysis approach. This stakeholder is the:",
        "opciones": [
            "Regulator",
            "Sponsor",
            "Tester",
            "End User"
        ],
        "respuesta": "Regulator",
        "explicacion": "A Regulator may impose constraints (such as required documentation or processes) that influence the business analysis approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which guideline or tool provides historical insight into the effectiveness of past business analysis work to inform the new approach?",
        "opciones": [
            "Business Analysis Performance Assessment",
            "Stakeholder Engagement Approach",
            "Information Management Approach",
            "Solution Scope"
        ],
        "respuesta": "Business Analysis Performance Assessment",
        "explicacion": "The Business Analysis Performance Assessment offers results from previous work that can help plan a more effective approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which guideline or tool refers to predefined sets of methods, processes, and standards used by an organization?",
        "opciones": [
            "Methodologies and Frameworks",
            "Expert Judgment",
            "Business Policies",
            "Legal/Regulatory Information"
        ],
        "respuesta": "Methodologies and Frameworks",
        "explicacion": "Methodologies and Frameworks shape the way business analysis work is approached, as organizations often adopt standard methods that the approach must align with.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "When planning the approach, 'Expert Judgment' is used to:",
        "opciones": [
            "Determine the optimal business analysis approach by drawing on experienced individuals",
            "Approve the final requirements package",
            "Define the change control process",
            "Calculate the return on investment of the solution"
        ],
        "respuesta": "Determine the optimal business analysis approach by drawing on experienced individuals",
        "explicacion": "Expert Judgment leverages the experience of internal or external experts (including past lessons) to select an appropriate approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which of the following best describes the 'Complexity and Risk' element?",
        "opciones": [
            "Adjusting the approach based on the size, complexity, and risk of the change and the initiative",
            "Identifying the risks of the proposed solution only",
            "Calculating the probability that the project finishes late",
            "Ranking requirements by business value"
        ],
        "respuesta": "Adjusting the approach based on the size, complexity, and risk of the change and the initiative",
        "explicacion": "Complexity and Risk considers the nature, size, complexity, and risk involved so that the approach can be adjusted accordingly.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which of the following is a recognized technique for the Plan Business Analysis Approach task?",
        "opciones": [
            "Lessons Learned",
            "Decision Modelling",
            "State Modelling",
            "Concept Modelling"
        ],
        "respuesta": "Lessons Learned",
        "explicacion": "Lessons Learned is among the techniques listed for this task; it captures insights from past work to improve the planned approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "In an adaptive environment, the planning of the business analysis approach is generally:",
        "opciones": [
            "Iterative and revisited throughout the initiative",
            "Completed once at the start and never changed",
            "Performed only by the sponsor",
            "Skipped entirely"
        ],
        "respuesta": "Iterative and revisited throughout the initiative",
        "explicacion": "Adaptive approaches plan iteratively, revisiting and refining the approach as the team learns more during the initiative.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which technique would a business analyst use to identify and evaluate uncertain events that could affect the chosen approach?",
        "opciones": [
            "Risk Analysis and Management",
            "Glossary",
            "Data Flow Diagrams",
            "Roles and Permissions Matrix"
        ],
        "respuesta": "Risk Analysis and Management",
        "explicacion": "Risk Analysis and Management is used to assess risks affecting the business analysis effort and to adjust the approach to mitigate them.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "The 'Business Analysis Activities' element is concerned with:",
        "opciones": [
            "Identifying the activities required and how they will be performed",
            "Deciding who approves requirements",
            "Determining where requirements are stored",
            "Setting the prioritization scheme"
        ],
        "respuesta": "Identifying the activities required and how they will be performed",
        "explicacion": "This element determines the specific activities needed to perform the business analysis work and how they will be carried out and integrated.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which of the following is NOT a stakeholder typically associated with the Plan Business Analysis Approach task?",
        "opciones": [
            "Supplier",
            "Domain Subject Matter Expert",
            "Project Manager",
            "Sponsor"
        ],
        "respuesta": "Supplier",
        "explicacion": "The stakeholders for this task are Domain SME, Project Manager, Regulator, and Sponsor. Supplier is not listed for this particular task.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Why does the business analyst consider the Stakeholder Engagement Approach as a guideline when planning the business analysis approach?",
        "opciones": [
            "The way stakeholders are engaged influences which activities and deliverables are appropriate",
            "It defines the final solution scope",
            "It establishes the project budget",
            "It is required to obtain regulatory approval"
        ],
        "respuesta": "The way stakeholders are engaged influences which activities and deliverables are appropriate",
        "explicacion": "Understanding how stakeholders will be engaged helps determine the activities, deliverables, and timing within the business analysis approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "A business analyst chooses to use workshops to collaboratively define the planned approach with key stakeholders. This is an example of which technique?",
        "opciones": [
            "Workshops",
            "Interviews",
            "Focus Groups",
            "Brainstorming"
        ],
        "respuesta": "Workshops",
        "explicacion": "Workshops bring stakeholders together to collaboratively define aspects of the business analysis approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which technique helps the business analyst track issues and decisions raised while defining the approach?",
        "opciones": [
            "Item Tracking",
            "Benchmarking and Market Analysis",
            "Vendor Assessment",
            "Sequence Diagrams"
        ],
        "respuesta": "Item Tracking",
        "explicacion": "Item Tracking records and manages issues, risks, and action items, including those that arise during planning of the approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "A 'hybrid' business analysis approach is best described as:",
        "opciones": [
            "A combination of predictive and adaptive elements selected to fit the initiative",
            "An approach that uses only predictive techniques",
            "An approach with no documentation",
            "An approach restricted to regulated industries"
        ],
        "respuesta": "A combination of predictive and adaptive elements selected to fit the initiative",
        "explicacion": "Many real initiatives use a hybrid approach, blending predictive and adaptive characteristics along the spectrum to suit the context.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which technique uses scope models to determine the boundaries of the planned business analysis work?",
        "opciones": [
            "Scope Modelling",
            "Process Modelling",
            "Data Modelling",
            "Organizational Modelling"
        ],
        "respuesta": "Scope Modelling",
        "explicacion": "Scope Modelling helps determine the boundaries and scope of the business analysis effort when planning the approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which technique provides a structured way to weigh financial costs and benefits when shaping the approach?",
        "opciones": [
            "Financial Analysis",
            "Survey or Questionnaire",
            "Mind Mapping",
            "Prototyping"
        ],
        "respuesta": "Financial Analysis",
        "explicacion": "Financial Analysis can support understanding the financial implications and value of the approach and the change being considered.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "When deciding the planning approach, the business analyst should consider all of the following EXCEPT:",
        "opciones": [
            "The detailed test scripts for the solution",
            "Organizational standards and methodologies",
            "The complexity and risk of the initiative",
            "Stakeholder location and availability"
        ],
        "respuesta": "The detailed test scripts for the solution",
        "explicacion": "Detailed test scripts are part of solution validation/testing, not a factor used to choose the business analysis planning approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "An organization mandates a specific waterfall methodology for all projects. How does this affect Plan Business Analysis Approach?",
        "opciones": [
            "It constrains the approach toward a more predictive, formally documented style",
            "It requires the business analyst to ignore organizational standards",
            "It forces an adaptive, minimal-documentation approach",
            "It has no effect on the approach"
        ],
        "respuesta": "It constrains the approach toward a more predictive, formally documented style",
        "explicacion": "Organizational methodologies and frameworks constrain the approach; a mandated waterfall method pushes toward predictive planning with formal deliverables.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "The Domain Subject Matter Expert contributes to planning the approach primarily by:",
        "opciones": [
            "Providing insight into the level of effort and complexity in their domain",
            "Approving the project budget",
            "Defining the change control process",
            "Selecting the storage tool for requirements"
        ],
        "respuesta": "Providing insight into the level of effort and complexity in their domain",
        "explicacion": "Domain SMEs help the business analyst understand domain complexity, which informs the activities, timing, and effort in the approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which of the following best characterizes the difference between predictive and adaptive deliverable formality?",
        "opciones": [
            "Predictive favors formal upfront deliverables; adaptive favors just-in-time, lighter deliverables",
            "Predictive uses no deliverables; adaptive uses formal deliverables",
            "Both require identical formality",
            "Adaptive requires more documentation than predictive"
        ],
        "respuesta": "Predictive favors formal upfront deliverables; adaptive favors just-in-time, lighter deliverables",
        "explicacion": "Predictive approaches produce formal deliverables early; adaptive approaches produce lighter deliverables on a just-in-time basis as needed.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Brainstorming is used in this task to:",
        "opciones": [
            "Generate ideas about possible approaches and activities",
            "Approve requirements formally",
            "Document the final traceability matrix",
            "Calculate financial returns"
        ],
        "respuesta": "Generate ideas about possible approaches and activities",
        "explicacion": "Brainstorming generates a range of options and ideas about how the business analysis work might be approached.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "The Sponsor's main interest in the business analysis approach is typically:",
        "opciones": [
            "Ensuring the approach supports delivering the expected business value within constraints",
            "Writing detailed requirements personally",
            "Storing the requirements repository",
            "Performing risk analysis calculations"
        ],
        "respuesta": "Ensuring the approach supports delivering the expected business value within constraints",
        "explicacion": "The Sponsor authorizes and funds the work and is concerned that the approach supports achieving the desired value within time and cost constraints.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Process Modelling is used when planning the approach to:",
        "opciones": [
            "Define and document the business analysis process to be followed",
            "Build the production system",
            "Approve change requests",
            "Estimate financial returns"
        ],
        "respuesta": "Define and document the business analysis process to be followed",
        "explicacion": "Process Modelling can describe and document the planned business analysis process and how activities flow together.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which statement about the business analysis approach is TRUE?",
        "opciones": [
            "It defines how and when tasks will be performed and the techniques used",
            "It is identical across all initiatives in an organization",
            "It only exists in adaptive projects",
            "It replaces the need for stakeholder engagement planning"
        ],
        "respuesta": "It defines how and when tasks will be performed and the techniques used",
        "explicacion": "The Business Analysis Approach specifies the activities, their timing, the techniques used, and the deliverables produced.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Surveys or questionnaires might be used in this task to:",
        "opciones": [
            "Gather input from many stakeholders about preferences for the approach",
            "Formally approve the requirements baseline",
            "Build the traceability matrix",
            "Define solution scope"
        ],
        "respuesta": "Gather input from many stakeholders about preferences for the approach",
        "explicacion": "A Survey or Questionnaire can collect input from a large or dispersed group of stakeholders to inform the planned approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which of the following would most strongly push an initiative toward an adaptive approach?",
        "opciones": [
            "High uncertainty in requirements and a need to deliver value early",
            "Strict regulatory documentation requirements",
            "A fixed, fully understood scope with low risk of change",
            "Mandated formal sign-off of all requirements upfront"
        ],
        "respuesta": "High uncertainty in requirements and a need to deliver value early",
        "explicacion": "Adaptive approaches suit situations of high uncertainty where delivering value early and refining requirements iteratively is beneficial.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Interviews support the Plan Business Analysis Approach task by:",
        "opciones": [
            "Eliciting individual stakeholder perspectives on the appropriate approach",
            "Replacing the need for a sponsor",
            "Generating the requirements baseline",
            "Defining acceptance criteria for the solution"
        ],
        "respuesta": "Eliciting individual stakeholder perspectives on the appropriate approach",
        "explicacion": "Interviews gather one-on-one perspectives from stakeholders that help shape an appropriate business analysis approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Reviews are used in this task primarily to:",
        "opciones": [
            "Evaluate and confirm the planned approach with stakeholders",
            "Conduct user acceptance testing",
            "Approve the solution scope",
            "Define the requirements attributes"
        ],
        "respuesta": "Evaluate and confirm the planned approach with stakeholders",
        "explicacion": "Reviews allow stakeholders to assess the proposed approach and confirm it is appropriate before work proceeds.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "A Business Case is used as a technique in this task to:",
        "opciones": [
            "Understand the justification and constraints that shape the approach",
            "Build the data model",
            "Track open issues",
            "Define stakeholder personas"
        ],
        "respuesta": "Understand the justification and constraints that shape the approach",
        "explicacion": "The Business Case provides context on the justification, expected value, and constraints, which influence the planned approach.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which best describes how 'Needs' shapes the business analysis approach?",
        "opciones": [
            "The nature of the underlying problem or opportunity drives the planned activities and rigor",
            "Needs determine who stores the requirements",
            "Needs are irrelevant to planning the approach",
            "Needs only matter in adaptive projects"
        ],
        "respuesta": "The nature of the underlying problem or opportunity drives the planned activities and rigor",
        "explicacion": "Since Needs is the only input, the problem or opportunity being addressed directly informs the approach, including activities, deliverables, and rigor.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "When a change is large, complex, and high-risk, the planned approach should generally include:",
        "opciones": [
            "More formal deliverables and rigorous activities",
            "Fewer activities and no documentation",
            "Only verbal communication",
            "No stakeholder involvement"
        ],
        "respuesta": "More formal deliverables and rigorous activities",
        "explicacion": "Higher complexity and risk call for greater rigor and formality in business analysis activities and deliverables.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which of the following correctly pairs an element with its concern?",
        "opciones": [
            "Planning Approach — whether predictive, adaptive, or hybrid",
            "Acceptance — where requirements are stored",
            "Timing — who approves the requirements",
            "Complexity and Risk — the prioritization scheme"
        ],
        "respuesta": "Planning Approach — whether predictive, adaptive, or hybrid",
        "explicacion": "The Planning Approach element decides the overall style (predictive, adaptive, or a hybrid) of conducting the business analysis work.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "The level of detail in business analysis deliverables should be driven primarily by:",
        "opciones": [
            "Stakeholder needs, organizational standards, and the nature of the change",
            "The personal preference of the business analyst only",
            "The size of the software development team",
            "The number of vendors involved"
        ],
        "respuesta": "Stakeholder needs, organizational standards, and the nature of the change",
        "explicacion": "Formality and level of detail are chosen based on stakeholder needs, organizational requirements, and the nature and risk of the change.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "The output 'Business Analysis Approach' is later used as an input to which other planning tasks?",
        "opciones": [
            "Plan Stakeholder Engagement, Plan Business Analysis Governance, and Plan Business Analysis Information Management",
            "Only Plan Stakeholder Engagement",
            "Only Identify Business Analysis Performance Improvements",
            "None; it is a final output"
        ],
        "respuesta": "Plan Stakeholder Engagement, Plan Business Analysis Governance, and Plan Business Analysis Information Management",
        "explicacion": "The Business Analysis Approach feeds the other planning tasks, providing the foundation upon which engagement, governance, and information management are planned.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    {
        "pregunta": "Which is the BEST reason to revisit the business analysis approach mid-initiative?",
        "opciones": [
            "Performance feedback or changing conditions indicate the current approach is no longer effective",
            "The sponsor wants to reduce stakeholder involvement permanently",
            "Documentation must always be eliminated halfway through",
            "The approach can never be revisited once approved"
        ],
        "respuesta": "Performance feedback or changing conditions indicate the current approach is no longer effective",
        "explicacion": "The approach can and should be adjusted when feedback or changing conditions reveal it is no longer effective, especially in adaptive contexts.",
        "tarea": "3.1 Plan Business Analysis Approach"
    },
    # ============================================================
    # 3.2 PLAN STAKEHOLDER ENGAGEMENT  (Q51-Q100)
    # ============================================================
    {
        "pregunta": "What is the purpose of the Plan Stakeholder Engagement task?",
        "opciones": [
            "To plan an approach for establishing and maintaining effective working relationships with stakeholders",
            "To store and manage business analysis information",
            "To define how requirements are approved",
            "To measure business analysis performance"
        ],
        "respuesta": "To plan an approach for establishing and maintaining effective working relationships with stakeholders",
        "explicacion": "Plan Stakeholder Engagement plans an approach for establishing and maintaining effective working relationships with the stakeholders.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which is the output of the Plan Stakeholder Engagement task?",
        "opciones": [
            "Stakeholder Engagement Approach",
            "Business Analysis Approach",
            "Governance Approach",
            "Business Analysis Performance Assessment"
        ],
        "respuesta": "Stakeholder Engagement Approach",
        "explicacion": "The output is the Stakeholder Engagement Approach, which records the analysis of stakeholders and the collaboration and communication approaches.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which are the inputs to the Plan Stakeholder Engagement task?",
        "opciones": [
            "Needs and Business Analysis Approach",
            "Needs only",
            "Governance Approach and Needs",
            "Requirements and Designs"
        ],
        "respuesta": "Needs and Business Analysis Approach",
        "explicacion": "The inputs are Needs (to identify affected stakeholders) and the Business Analysis Approach (which influences how stakeholders are engaged).",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which of the following is an element of the Plan Stakeholder Engagement task?",
        "opciones": [
            "Perform Stakeholder Analysis",
            "Plan Traceability Approach",
            "Decision Making",
            "Assessment Measures"
        ],
        "respuesta": "Perform Stakeholder Analysis",
        "explicacion": "Elements include Perform Stakeholder Analysis, Define Stakeholder Collaboration, and Stakeholder Communication Needs.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Stakeholder analysis involves identifying all of the following EXCEPT:",
        "opciones": [
            "The storage location of requirements",
            "Stakeholder roles",
            "Stakeholder attitudes",
            "Stakeholder level of power or influence"
        ],
        "respuesta": "The storage location of requirements",
        "explicacion": "Stakeholder analysis identifies roles, attitudes, decision-making authority, and level of power or influence. Storage of requirements is addressed in information management.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which tool plots stakeholders by their level of power against their level of interest or influence?",
        "opciones": [
            "Stakeholder matrix",
            "RACI matrix",
            "Onion diagram",
            "Context diagram"
        ],
        "respuesta": "Stakeholder matrix",
        "explicacion": "A stakeholder matrix (often a power/interest or power/influence grid) maps stakeholders to determine engagement intensity.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which technique uses a diagram of concentric circles to show how stakeholders relate to the solution and to one another?",
        "opciones": [
            "Onion diagram",
            "Stakeholder matrix",
            "Mind map",
            "Fishbone diagram"
        ],
        "respuesta": "Onion diagram",
        "explicacion": "The onion diagram shows stakeholders in concentric rings according to their involvement with and proximity to the solution.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "A RACI matrix is used during stakeholder analysis to:",
        "opciones": [
            "Define who is Responsible, Accountable, Consulted, and Informed",
            "Map stakeholders by power and interest",
            "Show concentric rings of stakeholder involvement",
            "Calculate the project's net present value"
        ],
        "respuesta": "Define who is Responsible, Accountable, Consulted, and Informed",
        "explicacion": "RACI clarifies stakeholder responsibilities by labeling each as Responsible, Accountable, Consulted, or Informed for activities or deliverables.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "The 'Define Stakeholder Collaboration' element addresses:",
        "opciones": [
            "How stakeholders will work together throughout the initiative",
            "Where requirements are physically stored",
            "Who has authority to approve requirements",
            "The metrics used to measure business analysis"
        ],
        "respuesta": "How stakeholders will work together throughout the initiative",
        "explicacion": "Define Stakeholder Collaboration plans how stakeholders will collaborate to keep them engaged and productive across the work.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "The 'Stakeholder Communication Needs' element is concerned with:",
        "opciones": [
            "What needs to be communicated, to whom, when, how, and in what format",
            "How requirements are prioritized",
            "Which methodology the team uses",
            "Where the requirements repository resides"
        ],
        "respuesta": "What needs to be communicated, to whom, when, how, and in what format",
        "explicacion": "Stakeholder Communication Needs determines the content, audience, timing, frequency, location, and format of communications.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which technique produces a list, map, or personas of stakeholders to support engagement planning?",
        "opciones": [
            "Stakeholder List, Map, or Personas",
            "Decision Analysis",
            "Acceptance and Evaluation Criteria",
            "Metrics and Key Performance Indicators"
        ],
        "respuesta": "Stakeholder List, Map, or Personas",
        "explicacion": "Stakeholder List, Map, or Personas identifies and categorizes stakeholders and their characteristics to plan engagement.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "A persona is best described as:",
        "opciones": [
            "A fictional but realistic profile representing a stakeholder group",
            "A formal approval document",
            "A risk register entry",
            "A traceability link"
        ],
        "respuesta": "A fictional but realistic profile representing a stakeholder group",
        "explicacion": "Personas are fictional characters created to represent the goals, needs, and behaviors of a stakeholder or user group.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Why is the Business Analysis Approach an input to stakeholder engagement planning?",
        "opciones": [
            "It influences the type and timing of stakeholder engagement and deliverables",
            "It stores the stakeholder list",
            "It approves the engagement plan",
            "It is unrelated and only included for completeness"
        ],
        "respuesta": "It influences the type and timing of stakeholder engagement and deliverables",
        "explicacion": "The Business Analysis Approach affects which stakeholders are engaged, how, and when, so it informs the engagement approach.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "A stakeholder with high power and high interest in the initiative should generally be:",
        "opciones": [
            "Managed closely and engaged frequently",
            "Ignored until the end of the project",
            "Only informed via mass email",
            "Excluded from decisions"
        ],
        "respuesta": "Managed closely and engaged frequently",
        "explicacion": "High-power, high-interest stakeholders require close management and active engagement because they can strongly affect outcomes.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which technique analyzes the organizational structure to understand stakeholder relationships and reporting lines?",
        "opciones": [
            "Organizational Modelling",
            "Data Modelling",
            "Process Modelling",
            "Sequence Diagrams"
        ],
        "respuesta": "Organizational Modelling",
        "explicacion": "Organizational Modelling depicts roles, responsibilities, and reporting structures, helping identify and understand stakeholders.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Stakeholder 'attitude' analysis examines stakeholders' feelings toward all of the following EXCEPT:",
        "opciones": [
            "The storage tool used for requirements",
            "The goals of the initiative",
            "The business analyst",
            "Collaboration and the chosen approach"
        ],
        "respuesta": "The storage tool used for requirements",
        "explicacion": "Attitude analysis looks at stakeholders' attitudes toward the business goals, the solution, the business analyst, collaboration, and the approach—not the requirements storage tool.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Why might the level of engagement differ between stakeholders?",
        "opciones": [
            "Because their power, influence, interest, and impact on the initiative differ",
            "Because all stakeholders must be engaged identically",
            "Because only the sponsor matters",
            "Because engagement is decided randomly"
        ],
        "respuesta": "Because their power, influence, interest, and impact on the initiative differ",
        "explicacion": "Engagement intensity is tailored to each stakeholder's power, influence, interest, and how the change affects them.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which technique can be used to identify stakeholders who could pose risks to the initiative if not engaged properly?",
        "opciones": [
            "Risk Analysis and Management",
            "Glossary",
            "Data Dictionary",
            "Functional Decomposition"
        ],
        "respuesta": "Risk Analysis and Management",
        "explicacion": "Risk Analysis and Management helps identify stakeholder-related risks (e.g., resistance or lack of availability) and plan mitigation.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Brainstorming supports stakeholder engagement planning by:",
        "opciones": [
            "Helping to generate a comprehensive list of possible stakeholders",
            "Approving the communication plan",
            "Storing the stakeholder register",
            "Defining acceptance criteria"
        ],
        "respuesta": "Helping to generate a comprehensive list of possible stakeholders",
        "explicacion": "Brainstorming generates ideas, including a broad list of potential stakeholders who may be affected by or influence the change.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which technique examines existing materials such as org charts and project documents to identify stakeholders?",
        "opciones": [
            "Document Analysis",
            "Observation",
            "Prototyping",
            "Interface Analysis"
        ],
        "respuesta": "Document Analysis",
        "explicacion": "Document Analysis reviews existing documentation to discover stakeholders and understand their roles and relationships.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "A stakeholder's 'decision-making authority' refers to:",
        "opciones": [
            "The level of authority the stakeholder has over business analysis activities, decisions, deliverables, and the change",
            "Their physical location",
            "Their job title only",
            "The tool they use to communicate"
        ],
        "respuesta": "The level of authority the stakeholder has over business analysis activities, decisions, deliverables, and the change",
        "explicacion": "Decision-making authority indicates the extent of a stakeholder's authority over the work, decisions, deliverables, and the change itself.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Mind Mapping is used in stakeholder engagement planning to:",
        "opciones": [
            "Visually organize stakeholders and their relationships and characteristics",
            "Approve the requirements baseline",
            "Define the prioritization scheme",
            "Compute financial returns"
        ],
        "respuesta": "Visually organize stakeholders and their relationships and characteristics",
        "explicacion": "Mind Mapping can be used to brainstorm and visually structure information about stakeholders and their attributes.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which technique helps determine the boundaries of the solution and thereby which stakeholders are affected?",
        "opciones": [
            "Scope Modelling",
            "State Modelling",
            "Decision Modelling",
            "Concept Modelling"
        ],
        "respuesta": "Scope Modelling",
        "explicacion": "Scope Modelling defines solution boundaries, which helps identify stakeholders within or affected by that scope.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Business Rules Analysis can support stakeholder engagement planning by:",
        "opciones": [
            "Identifying stakeholders who own or are governed by relevant business rules",
            "Storing the requirements repository",
            "Approving the solution scope",
            "Defining the test plan"
        ],
        "respuesta": "Identifying stakeholders who own or are governed by relevant business rules",
        "explicacion": "Business Rules Analysis can reveal which stakeholders are responsible for, or affected by, the business rules in scope.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "In an adaptive environment, stakeholder collaboration tends to be:",
        "opciones": [
            "Frequent, informal, and direct",
            "Rare and heavily documented",
            "Limited to formal sign-off meetings",
            "Conducted only at project closure"
        ],
        "respuesta": "Frequent, informal, and direct",
        "explicacion": "Adaptive approaches emphasize frequent, direct, and often informal collaboration with stakeholders throughout iterations.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Why is identifying stakeholders early important?",
        "opciones": [
            "Missing stakeholders can lead to missed requirements and reduced solution value",
            "It guarantees the project finishes early",
            "It eliminates the need for governance",
            "It removes the need for documentation"
        ],
        "respuesta": "Missing stakeholders can lead to missed requirements and reduced solution value",
        "explicacion": "Failing to identify stakeholders risks overlooking needs and requirements, harming the solution's ability to deliver value.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "A 'supporter' stakeholder identified during attitude analysis is one who:",
        "opciones": [
            "Has a positive attitude toward the change and the business analysis effort",
            "Always blocks the initiative",
            "Has no influence on the outcome",
            "Cannot be communicated with"
        ],
        "respuesta": "Has a positive attitude toward the change and the business analysis effort",
        "explicacion": "Attitude analysis distinguishes supporters (positive) from those who are neutral or opposed, informing engagement tactics.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Interviews support stakeholder engagement planning primarily by:",
        "opciones": [
            "Gathering detailed information about stakeholders' roles, attitudes, and needs",
            "Approving the engagement approach",
            "Storing communications",
            "Computing risk scores"
        ],
        "respuesta": "Gathering detailed information about stakeholders' roles, attitudes, and needs",
        "explicacion": "Interviews elicit detailed insight from or about stakeholders, helping refine the engagement and communication plan.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Surveys or questionnaires are particularly useful in stakeholder engagement planning when:",
        "opciones": [
            "There are many stakeholders who are geographically dispersed",
            "Only one stakeholder needs to be consulted",
            "No stakeholders have been identified yet",
            "The sponsor forbids communication"
        ],
        "respuesta": "There are many stakeholders who are geographically dispersed",
        "explicacion": "Surveys efficiently collect information from large or dispersed stakeholder groups about their needs and preferences.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Process Modelling can aid stakeholder engagement planning by:",
        "opciones": [
            "Revealing the people who perform or are affected by the processes in scope",
            "Approving the final requirements",
            "Defining where requirements are stored",
            "Calculating ROI"
        ],
        "respuesta": "Revealing the people who perform or are affected by the processes in scope",
        "explicacion": "Process models show roles and actors involved in processes, helping identify stakeholders to engage.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Workshops contribute to stakeholder engagement planning by:",
        "opciones": [
            "Bringing stakeholders together to collaboratively shape the engagement approach",
            "Replacing the need to identify stakeholders",
            "Storing the communication plan",
            "Approving the project budget"
        ],
        "respuesta": "Bringing stakeholders together to collaboratively shape the engagement approach",
        "explicacion": "Workshops gather multiple stakeholders to collaborate, which can also reveal relationships and inform the engagement approach.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which of the following best describes the relationship between Needs and stakeholder identification?",
        "opciones": [
            "Understanding the Needs helps determine which stakeholders are impacted and should be engaged",
            "Needs are irrelevant to identifying stakeholders",
            "Needs only matter after the solution is built",
            "Needs are an output, not an input"
        ],
        "respuesta": "Understanding the Needs helps determine which stakeholders are impacted and should be engaged",
        "explicacion": "The Needs being addressed indicate which stakeholders are affected and therefore who should be engaged.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "A stakeholder who is highly impacted by the change but has low influence should typically be:",
        "opciones": [
            "Kept informed and consulted as appropriate",
            "Completely ignored",
            "Given final approval authority",
            "Removed from the stakeholder list"
        ],
        "respuesta": "Kept informed and consulted as appropriate",
        "explicacion": "Highly impacted but low-influence stakeholders are usually kept informed and consulted so their needs are considered.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "The Stakeholder Engagement Approach is later used as a guideline or input by which other tasks?",
        "opciones": [
            "Other planning and elicitation/collaboration tasks across the BABOK",
            "Only the Plan Business Analysis Approach task",
            "Only Identify Business Analysis Performance Improvements",
            "No other tasks"
        ],
        "respuesta": "Other planning and elicitation/collaboration tasks across the BABOK",
        "explicacion": "The Stakeholder Engagement Approach informs subsequent tasks such as governance and information management planning, and elicitation and collaboration activities.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which factor would most increase the complexity of stakeholder engagement?",
        "opciones": [
            "A large number of stakeholders with conflicting interests across geographies",
            "A single co-located stakeholder",
            "A short, low-impact change",
            "A team that meets in one room daily"
        ],
        "respuesta": "A large number of stakeholders with conflicting interests across geographies",
        "explicacion": "Many stakeholders, conflicting interests, and geographic dispersion all increase the complexity of engagement.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "The frequency and formality of stakeholder communication should be based on:",
        "opciones": [
            "Stakeholder needs, the approach, and the nature of the information",
            "The business analyst's personal schedule only",
            "A fixed weekly cadence for all stakeholders regardless of need",
            "The size of the development team"
        ],
        "respuesta": "Stakeholder needs, the approach, and the nature of the information",
        "explicacion": "Communication frequency and formality are tailored to stakeholder needs, the chosen approach, and the type of information.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which of the following is TRUE about the Stakeholder List, Map, or Personas technique?",
        "opciones": [
            "It can range from a simple list to a detailed map or set of personas depending on need",
            "It must always be a formal RACI matrix",
            "It is only used in predictive projects",
            "It replaces the need for stakeholder analysis"
        ],
        "respuesta": "It can range from a simple list to a detailed map or set of personas depending on need",
        "explicacion": "This technique scales from a simple stakeholder list to richer maps or personas based on the complexity of the engagement.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "A key risk addressed during stakeholder engagement planning is:",
        "opciones": [
            "Insufficient stakeholder availability or commitment",
            "The choice of programming language",
            "The database vendor",
            "The office floor plan"
        ],
        "respuesta": "Insufficient stakeholder availability or commitment",
        "explicacion": "Stakeholder availability and commitment are common engagement risks the plan should anticipate and mitigate.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Stakeholders may be identified at different levels, including:",
        "opciones": [
            "Individuals, groups, or organizations",
            "Only individuals",
            "Only the project team",
            "Only the sponsor and regulator"
        ],
        "respuesta": "Individuals, groups, or organizations",
        "explicacion": "Stakeholders can be individuals, groups, or entire organizations affected by or influencing the change.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "When a stakeholder's attitude is negative or resistant, the engagement approach should:",
        "opciones": [
            "Include tactics to understand concerns and build support",
            "Exclude them entirely from the initiative",
            "Avoid any communication with them",
            "Grant them full approval authority to placate them"
        ],
        "respuesta": "Include tactics to understand concerns and build support",
        "explicacion": "Negative attitudes should be managed by understanding concerns and using tactics to gain support and reduce resistance.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which of the following is NOT typically part of the Stakeholder Engagement Approach output?",
        "opciones": [
            "The requirements traceability matrix",
            "Stakeholder roles and responsibilities",
            "Collaboration approach",
            "Communication needs"
        ],
        "respuesta": "The requirements traceability matrix",
        "explicacion": "Traceability is part of information management, not the Stakeholder Engagement Approach, which covers stakeholder analysis, collaboration, and communication.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "A stakeholder who must be 'Accountable' on a RACI matrix:",
        "opciones": [
            "Is ultimately answerable for the correct completion of the activity",
            "Merely performs the work",
            "Is only consulted for opinions",
            "Is only kept informed of progress"
        ],
        "respuesta": "Is ultimately answerable for the correct completion of the activity",
        "explicacion": "In RACI, the Accountable party is ultimately answerable; there should be exactly one Accountable role per activity.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "The level of effort spent on stakeholder analysis should be:",
        "opciones": [
            "Proportional to the complexity of the change and the stakeholder community",
            "Identical for every initiative",
            "Always minimal regardless of context",
            "Decided solely by the sponsor"
        ],
        "respuesta": "Proportional to the complexity of the change and the stakeholder community",
        "explicacion": "Effort on stakeholder analysis scales with the complexity of the change and the number and diversity of stakeholders.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which is the BEST description of 'stakeholder collaboration'?",
        "opciones": [
            "Stakeholders willingly participating and working together toward shared objectives",
            "Stakeholders signing approval documents only",
            "Stakeholders receiving status reports passively",
            "Stakeholders being excluded to speed delivery"
        ],
        "respuesta": "Stakeholders willingly participating and working together toward shared objectives",
        "explicacion": "Collaboration is active, willing participation among stakeholders to achieve common goals throughout the initiative.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "If a stakeholder is identified late in the initiative, the most likely consequence is:",
        "opciones": [
            "Rework due to previously unidentified needs or requirements",
            "Faster delivery of the solution",
            "Reduced project cost",
            "No impact whatsoever"
        ],
        "respuesta": "Rework due to previously unidentified needs or requirements",
        "explicacion": "Late identification often surfaces new needs and requirements, causing rework and potential schedule and cost impacts.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which dimension of stakeholder analysis would best explain why a particular stakeholder can veto a decision?",
        "opciones": [
            "Decision-making authority",
            "Geographic location",
            "Communication format preference",
            "Attitude toward the business analyst"
        ],
        "respuesta": "Decision-making authority",
        "explicacion": "A stakeholder's decision-making authority determines the extent of control they have, including the power to approve or veto decisions.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Tailoring communication 'format' for stakeholders means choosing between options such as:",
        "opciones": [
            "Formal reports, informal emails, presentations, or face-to-face discussions",
            "Predictive versus adaptive methodologies",
            "Power versus interest grids",
            "Traceability versus reuse"
        ],
        "respuesta": "Formal reports, informal emails, presentations, or face-to-face discussions",
        "explicacion": "Format options include formal documents, informal messages, presentations, and verbal/face-to-face communication tailored to each audience.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which statement about stakeholder engagement planning in adaptive contexts is TRUE?",
        "opciones": [
            "Engagement is typically continuous and revisited each iteration",
            "It is fixed at the start and never revisited",
            "It is unnecessary because the team is small",
            "It is handled entirely by the regulator"
        ],
        "respuesta": "Engagement is typically continuous and revisited each iteration",
        "explicacion": "Adaptive approaches treat stakeholder engagement as ongoing, revisiting and adjusting it throughout iterations.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    # ============================================================
    # 3.3 PLAN BUSINESS ANALYSIS GOVERNANCE  (Q101-Q150)
    # ============================================================
    {
        "pregunta": "What is the purpose of the Plan Business Analysis Governance task?",
        "opciones": [
            "To define how decisions are made about requirements and designs, including reviews, change control, approvals, and prioritization",
            "To elicit requirements from stakeholders",
            "To store and reuse business analysis information",
            "To measure business analysis performance"
        ],
        "respuesta": "To define how decisions are made about requirements and designs, including reviews, change control, approvals, and prioritization",
        "explicacion": "Plan Business Analysis Governance defines how decisions are made and how requirements and designs are approved, prioritized, and changed.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which is the output of the Plan Business Analysis Governance task?",
        "opciones": [
            "Governance Approach",
            "Stakeholder Engagement Approach",
            "Business Analysis Approach",
            "Information Management Approach"
        ],
        "respuesta": "Governance Approach",
        "explicacion": "The output is the Governance Approach, which defines decision making, change control, prioritization, and approvals.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "What is the input to the Plan Business Analysis Governance task?",
        "opciones": [
            "Business Analysis Approach",
            "Needs",
            "Requirements",
            "Designs"
        ],
        "respuesta": "Business Analysis Approach",
        "explicacion": "The Business Analysis Approach is the input; it shapes how governance is planned for the initiative.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which of the following is an element of the Plan Business Analysis Governance task?",
        "opciones": [
            "Change Control Process",
            "Stakeholder Communication Needs",
            "Plan Traceability Approach",
            "Assessment Measures"
        ],
        "respuesta": "Change Control Process",
        "explicacion": "Elements are Decision Making, Change Control Process, Plan Prioritization Approach, and Plan for Approvals.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "The 'Decision Making' element defines:",
        "opciones": [
            "The roles stakeholders play in decisions and how decisions are reached",
            "Where requirements are stored",
            "How performance is measured",
            "The communication format for each stakeholder"
        ],
        "respuesta": "The roles stakeholders play in decisions and how decisions are reached",
        "explicacion": "Decision Making defines the roles of stakeholders in making decisions, who participates, who is the decision maker, and how decisions are escalated and resolved.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "The 'Change Control Process' element addresses:",
        "opciones": [
            "How proposed changes to requirements and designs are requested, evaluated, and decided",
            "How requirements are physically stored",
            "How stakeholders are identified",
            "How business analysis performance is improved"
        ],
        "respuesta": "How proposed changes to requirements and designs are requested, evaluated, and decided",
        "explicacion": "The Change Control Process defines how changes to requirements and designs will be requested, analyzed for impact, and approved or rejected.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which element determines how requirements and designs are ranked when not all can be implemented at once?",
        "opciones": [
            "Plan Prioritization Approach",
            "Plan for Approvals",
            "Decision Making",
            "Change Control Process"
        ],
        "respuesta": "Plan Prioritization Approach",
        "explicacion": "Plan Prioritization Approach establishes the timing, formality, criteria, and process for prioritizing requirements and designs.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "The 'Plan for Approvals' element defines:",
        "opciones": [
            "The timing, frequency, and process by which requirements and designs are approved",
            "Where requirements are stored",
            "Which metrics measure performance",
            "How stakeholders collaborate informally"
        ],
        "respuesta": "The timing, frequency, and process by which requirements and designs are approved",
        "explicacion": "Plan for Approvals determines the type of approvals needed, the timing and frequency, and who approves requirements and designs.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "A formal change control process typically requires a change request to include:",
        "opciones": [
            "An impact assessment and a recommendation",
            "Only the requester's name",
            "Only a verbal description",
            "Nothing beyond approval"
        ],
        "respuesta": "An impact assessment and a recommendation",
        "explicacion": "Effective change control documents the proposed change, assesses its impact (cost, schedule, benefits), and provides a recommendation for the decision.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which elements should a change request typically capture?",
        "opciones": [
            "Cost and time estimates, benefits, risks, and priority of the change",
            "Only the date it was submitted",
            "Only the storage location",
            "Only the stakeholder's job title"
        ],
        "respuesta": "Cost and time estimates, benefits, risks, and priority of the change",
        "explicacion": "A change request typically records estimated cost and time, benefits, risks, and the priority to support an informed decision.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "In a more adaptive governance approach, change control is usually:",
        "opciones": [
            "Less formal, with changes handled through reprioritization of the backlog",
            "Extremely formal with multiple sign-offs for every change",
            "Forbidden entirely",
            "Decided only by the regulator"
        ],
        "respuesta": "Less formal, with changes handled through reprioritization of the backlog",
        "explicacion": "Adaptive governance often handles change informally by reprioritizing the backlog rather than processing each change through a formal board.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Who is typically the 'decision maker' for requirements approval?",
        "opciones": [
            "The stakeholder with the appropriate authority, often the sponsor or designated owner",
            "Any team member at random",
            "The business analyst alone in all cases",
            "The end users collectively in all cases"
        ],
        "respuesta": "The stakeholder with the appropriate authority, often the sponsor or designated owner",
        "explicacion": "Approval authority rests with the stakeholder(s) who have the right level of authority, frequently the sponsor or product/requirement owner.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which technique is used to evaluate the proposed governance process with stakeholders?",
        "opciones": [
            "Reviews",
            "Data Modelling",
            "Prototyping",
            "Interface Analysis"
        ],
        "respuesta": "Reviews",
        "explicacion": "Reviews assess whether the proposed governance approach is appropriate and obtain stakeholder agreement on it.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Item Tracking supports governance planning by:",
        "opciones": [
            "Managing issues and risks related to governance decisions",
            "Storing the requirements repository",
            "Approving the solution",
            "Building the data model"
        ],
        "respuesta": "Managing issues and risks related to governance decisions",
        "explicacion": "Item Tracking records and follows up on issues and risks, including those arising from governance and decision-making activities.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which technique analyzes the organization to determine who holds decision-making authority?",
        "opciones": [
            "Organizational Modelling",
            "Scope Modelling",
            "Data Flow Diagrams",
            "Sequence Diagrams"
        ],
        "respuesta": "Organizational Modelling",
        "explicacion": "Organizational Modelling reveals roles, reporting lines, and authority, helping define decision-making and approval responsibilities.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Why is the Business Analysis Approach an input to governance planning?",
        "opciones": [
            "It indicates the formality and rigor that the governance process should match",
            "It stores the change log",
            "It approves all requirements",
            "It is unrelated to governance"
        ],
        "respuesta": "It indicates the formality and rigor that the governance process should match",
        "explicacion": "The Business Analysis Approach (predictive vs. adaptive, formality, deliverables) shapes how formal and rigorous the governance approach should be.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Prioritization criteria for requirements might include all of the following EXCEPT:",
        "opciones": [
            "The font used in the requirements document",
            "Business value",
            "Implementation difficulty",
            "Risk and regulatory or policy compliance"
        ],
        "respuesta": "The font used in the requirements document",
        "explicacion": "Prioritization considers value, cost, difficulty, risk, dependencies, and compliance—not document formatting choices.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "A regulated environment most likely requires a governance approach that is:",
        "opciones": [
            "More formal, with documented approvals and an auditable change trail",
            "Entirely informal with no documentation",
            "Free of any approval steps",
            "Decided solely by end users"
        ],
        "respuesta": "More formal, with documented approvals and an auditable change trail",
        "explicacion": "Regulatory contexts demand formal, documented approvals and traceable change records to satisfy compliance and audit needs.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "What does the governance approach define regarding approvals?",
        "opciones": [
            "What must be approved, by whom, when, and how",
            "Only the storage tool for requirements",
            "Only the prioritization technique",
            "Only stakeholder personas"
        ],
        "respuesta": "What must be approved, by whom, when, and how",
        "explicacion": "The approval portion of the governance approach specifies which deliverables need approval, the approvers, timing, and process.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Lessons Learned is used in governance planning to:",
        "opciones": [
            "Apply insights from previous initiatives to design a better governance process",
            "Approve the current requirements",
            "Store requirement attributes",
            "Calculate ROI"
        ],
        "respuesta": "Apply insights from previous initiatives to design a better governance process",
        "explicacion": "Lessons Learned brings forward what worked or failed in past governance to improve the current approach.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "A change control board (CCB) is an example of:",
        "opciones": [
            "A governance mechanism for evaluating and deciding on proposed changes",
            "A requirements storage tool",
            "A stakeholder persona",
            "A prioritization technique"
        ],
        "respuesta": "A governance mechanism for evaluating and deciding on proposed changes",
        "explicacion": "A change control board is a governance body that reviews change requests and decides whether to approve, reject, or defer them.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which of the following stakeholders is associated with the Plan Business Analysis Governance task?",
        "opciones": [
            "Sponsor",
            "Tester",
            "Operational Support",
            "Supplier"
        ],
        "respuesta": "Sponsor",
        "explicacion": "Stakeholders for this task include Domain SME, Project Manager, Regulator, and Sponsor.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Process Modelling supports governance planning by:",
        "opciones": [
            "Documenting the decision-making, change control, and approval processes",
            "Storing the requirements",
            "Approving the solution scope",
            "Defining stakeholder personas"
        ],
        "respuesta": "Documenting the decision-making, change control, and approval processes",
        "explicacion": "Process Modelling can depict the governance processes (decision making, change control, approvals) so they are clear and repeatable.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which is the BEST description of 'decision-making escalation'?",
        "opciones": [
            "A defined path for resolving decisions that cannot be made at the current level",
            "Storing decisions in a repository",
            "Prioritizing requirements by value",
            "Communicating decisions to all stakeholders"
        ],
        "respuesta": "A defined path for resolving decisions that cannot be made at the current level",
        "explicacion": "Escalation defines how unresolved decisions move to higher authority levels until resolved.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Interviews can support governance planning by:",
        "opciones": [
            "Eliciting stakeholder views on decision rights, approvals, and change handling",
            "Storing the change log",
            "Building the traceability matrix",
            "Computing risk scores automatically"
        ],
        "respuesta": "Eliciting stakeholder views on decision rights, approvals, and change handling",
        "explicacion": "Interviews gather stakeholder input on how decisions, approvals, and changes should be governed.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which best describes the relationship between prioritization and governance?",
        "opciones": [
            "Prioritization is a governed activity; the governance approach defines how prioritization decisions are made",
            "Prioritization has nothing to do with governance",
            "Governance forbids prioritization",
            "Prioritization replaces the need for approvals"
        ],
        "respuesta": "Prioritization is a governed activity; the governance approach defines how prioritization decisions are made",
        "explicacion": "Prioritization is part of governance: the approach sets out the criteria, timing, and process for making prioritization decisions.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "A well-defined approval process helps to:",
        "opciones": [
            "Establish a clear, agreed baseline of requirements and designs",
            "Eliminate the need for stakeholders",
            "Remove the requirement to elicit needs",
            "Avoid documenting any decisions"
        ],
        "respuesta": "Establish a clear, agreed baseline of requirements and designs",
        "explicacion": "Approvals create agreed baselines, providing a reference point against which changes are controlled.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Document Analysis supports governance planning by:",
        "opciones": [
            "Reviewing existing organizational governance policies and standards",
            "Approving the requirements baseline",
            "Storing the requirements",
            "Defining stakeholder communication formats"
        ],
        "respuesta": "Reviewing existing organizational governance policies and standards",
        "explicacion": "Document Analysis examines existing governance policies, standards, and templates that the new approach must align with.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "If two stakeholders disagree on a requirement and neither has overriding authority, the governance approach should provide:",
        "opciones": [
            "A conflict resolution and escalation mechanism",
            "Automatic approval of both versions",
            "Deletion of the requirement",
            "Indefinite deferral with no process"
        ],
        "respuesta": "A conflict resolution and escalation mechanism",
        "explicacion": "Governance should define how conflicts are resolved and how decisions escalate when stakeholders cannot agree.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which of the following is TRUE about the formality of the governance approach?",
        "opciones": [
            "It should be proportional to the complexity, risk, and regulatory context of the initiative",
            "It should always be maximally formal",
            "It should always be minimal",
            "It is unrelated to risk"
        ],
        "respuesta": "It should be proportional to the complexity, risk, and regulatory context of the initiative",
        "explicacion": "Governance formality is scaled to fit the complexity, risk, and regulatory demands of the specific initiative.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Workshops support governance planning by:",
        "opciones": [
            "Collaboratively defining decision rights, approval steps, and change processes with stakeholders",
            "Storing change requests",
            "Approving the final solution",
            "Calculating financial value"
        ],
        "respuesta": "Collaboratively defining decision rights, approval steps, and change processes with stakeholders",
        "explicacion": "Workshops bring stakeholders together to agree on governance details such as decision rights, approvals, and change handling.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "What is a key benefit of defining the change control process during planning rather than reactively?",
        "opciones": [
            "Changes can be handled consistently and their impacts understood before decisions",
            "It guarantees no changes will occur",
            "It removes the need for approvals",
            "It eliminates all project risk"
        ],
        "respuesta": "Changes can be handled consistently and their impacts understood before decisions",
        "explicacion": "Planning change control upfront ensures changes are evaluated consistently with understood impacts, avoiding ad hoc decisions.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Surveys or questionnaires can support governance planning by:",
        "opciones": [
            "Gathering input from many stakeholders on preferred decision and approval processes",
            "Approving the governance approach",
            "Storing decision records",
            "Building the prioritization model automatically"
        ],
        "respuesta": "Gathering input from many stakeholders on preferred decision and approval processes",
        "explicacion": "Surveys collect input from a broad stakeholder group about how governance, decisions, and approvals should operate.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which of the following best distinguishes 'decision making' from 'approvals' in governance?",
        "opciones": [
            "Decision making covers how all decisions are reached; approvals specifically concern formally accepting requirements and designs",
            "They are identical concepts",
            "Approvals occur before any decisions",
            "Decision making applies only to changes"
        ],
        "respuesta": "Decision making covers how all decisions are reached; approvals specifically concern formally accepting requirements and designs",
        "explicacion": "Decision making is the broader element about how decisions are made; approvals specifically address formally accepting deliverables.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Brainstorming is used in governance planning to:",
        "opciones": [
            "Generate options for decision-making and change control processes",
            "Approve requirements",
            "Store the requirements baseline",
            "Define traceability links"
        ],
        "respuesta": "Generate options for decision-making and change control processes",
        "explicacion": "Brainstorming generates ideas and options for how governance, decisions, and change control might be structured.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "The prioritization approach should specify the timing of prioritization, meaning:",
        "opciones": [
            "When and how often requirements will be prioritized during the initiative",
            "The font size of the priority labels",
            "Where the priorities are stored",
            "Who writes the requirements"
        ],
        "respuesta": "When and how often requirements will be prioritized during the initiative",
        "explicacion": "Timing addresses when prioritization occurs and how frequently it is revisited, which differs between predictive and adaptive contexts.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "In adaptive initiatives, prioritization is typically:",
        "opciones": [
            "Continuous, with the backlog reprioritized regularly",
            "Done once at the start and never changed",
            "Performed only by the regulator",
            "Avoided entirely"
        ],
        "respuesta": "Continuous, with the backlog reprioritized regularly",
        "explicacion": "Adaptive approaches reprioritize the backlog frequently as new information and changing value emerge.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which is an example of a governance decision about requirements?",
        "opciones": [
            "Approving a baseline set of requirements for development",
            "Choosing the requirements management tool's color scheme",
            "Selecting the office where stakeholders meet",
            "Deciding the developer's lunch schedule"
        ],
        "respuesta": "Approving a baseline set of requirements for development",
        "explicacion": "Approving a requirements baseline is a core governance decision about requirements and designs.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Why must the governance approach align with organizational policies?",
        "opciones": [
            "Governance must operate within existing organizational standards and constraints",
            "Organizational policies are irrelevant to projects",
            "Policies forbid all governance",
            "Alignment slows the project unnecessarily"
        ],
        "respuesta": "Governance must operate within existing organizational standards and constraints",
        "explicacion": "The governance approach must respect existing organizational policies, standards, and any regulatory constraints.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "A poorly defined change control process is most likely to result in:",
        "opciones": [
            "Scope creep and inconsistent handling of changes",
            "Faster delivery with no downside",
            "Automatic stakeholder agreement",
            "Elimination of all requirements"
        ],
        "respuesta": "Scope creep and inconsistent handling of changes",
        "explicacion": "Without clear change control, changes are handled inconsistently, often leading to uncontrolled scope creep.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Who typically has authority to approve changes that affect scope, budget, or schedule?",
        "opciones": [
            "The sponsor or an authorized governance body",
            "Any developer on the team",
            "The end users individually",
            "No one; such changes are automatic"
        ],
        "respuesta": "The sponsor or an authorized governance body",
        "explicacion": "Changes affecting scope, budget, or schedule usually require approval from the sponsor or a designated governance authority.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "The Governance Approach output is used as an input to which other planning task?",
        "opciones": [
            "Plan Business Analysis Information Management",
            "Plan Business Analysis Approach",
            "Plan Stakeholder Engagement",
            "It is not used by any other task"
        ],
        "respuesta": "Plan Business Analysis Information Management",
        "explicacion": "The Governance Approach feeds Plan Business Analysis Information Management, since governance influences how information and decisions are tracked.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which of the following would be considered a prioritization criterion?",
        "opciones": [
            "Dependencies between requirements",
            "The stakeholder's office location",
            "The brand of computer used",
            "The number of pages in the document"
        ],
        "respuesta": "Dependencies between requirements",
        "explicacion": "Dependencies are a legitimate prioritization criterion, alongside value, cost, risk, and difficulty.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "What is the role of the business analyst in the governance process?",
        "opciones": [
            "Often to facilitate and support governance activities, while decision authority rests with designated stakeholders",
            "To make all approval decisions unilaterally",
            "To avoid involvement in governance",
            "To override the sponsor's decisions"
        ],
        "respuesta": "Often to facilitate and support governance activities, while decision authority rests with designated stakeholders",
        "explicacion": "The business analyst typically facilitates governance (analysis, recommendations, tracking) while formal authority lies with designated decision makers.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "A 'baseline' in the context of governance is:",
        "opciones": [
            "An approved version of requirements or designs against which changes are measured",
            "The first draft of any document",
            "A list of stakeholders",
            "The project budget"
        ],
        "respuesta": "An approved version of requirements or designs against which changes are measured",
        "explicacion": "A baseline is an approved, fixed version used as a reference point; subsequent changes are controlled against it.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which question does the 'Plan for Approvals' element NOT directly answer?",
        "opciones": [
            "Where will requirements be physically stored?",
            "What requires approval?",
            "When will approvals occur?",
            "Who provides approval?"
        ],
        "respuesta": "Where will requirements be physically stored?",
        "explicacion": "Storage location is an information management concern. Plan for Approvals answers what, who, when, and how approvals happen.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "How should the change control process handle the impact of a proposed change?",
        "opciones": [
            "Assess impacts on benefits, cost, schedule, and other requirements before deciding",
            "Approve all changes without analysis",
            "Reject all changes by default",
            "Ignore impacts to save time"
        ],
        "respuesta": "Assess impacts on benefits, cost, schedule, and other requirements before deciding",
        "explicacion": "Sound change control evaluates the full impact of a change before a decision is made to approve, reject, or defer it.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which statement about decision making in governance is TRUE?",
        "opciones": [
            "It should clearly identify who participates, who decides, and how conflicts are resolved",
            "It should leave roles undefined for flexibility",
            "Only the business analyst should decide everything",
            "Decisions should never be documented"
        ],
        "respuesta": "It should clearly identify who participates, who decides, and how conflicts are resolved",
        "explicacion": "Effective decision making clarifies participation, the decision maker, and the path to resolve disagreements.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "A primary reason to plan governance early is to:",
        "opciones": [
            "Avoid ambiguity and delays when decisions, approvals, and changes arise later",
            "Guarantee zero changes will ever occur",
            "Replace stakeholder engagement",
            "Eliminate the need for elicitation"
        ],
        "respuesta": "Avoid ambiguity and delays when decisions, approvals, and changes arise later",
        "explicacion": "Planning governance early prevents confusion and delay by establishing clear decision, approval, and change processes in advance.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    # ============================================================
    # 3.4 PLAN BUSINESS ANALYSIS INFORMATION MANAGEMENT  (Q151-Q200)
    # ============================================================
    {
        "pregunta": "What is the purpose of the Plan Business Analysis Information Management task?",
        "opciones": [
            "To define how business analysis information will be stored, accessed, organized, and used",
            "To define how decisions are approved",
            "To measure business analysis performance",
            "To identify stakeholders"
        ],
        "respuesta": "To define how business analysis information will be stored, accessed, organized, and used",
        "explicacion": "This task defines how business analysis information (requirements, designs, models) will be captured, stored, organized, accessed, and managed.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which is the output of the Plan Business Analysis Information Management task?",
        "opciones": [
            "Information Management Approach",
            "Governance Approach",
            "Stakeholder Engagement Approach",
            "Business Analysis Approach"
        ],
        "respuesta": "Information Management Approach",
        "explicacion": "The output is the Information Management Approach, which defines how information is organized, traced, stored, accessed, and reused.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which are inputs to the Plan Business Analysis Information Management task?",
        "opciones": [
            "Business Analysis Approach, Governance Approach, and Stakeholder Engagement Approach",
            "Needs only",
            "Requirements and Designs",
            "Governance Approach only"
        ],
        "respuesta": "Business Analysis Approach, Governance Approach, and Stakeholder Engagement Approach",
        "explicacion": "The three inputs are the Business Analysis Approach, Governance Approach, and Stakeholder Engagement Approach.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which of the following is an element of this task?",
        "opciones": [
            "Plan Traceability Approach",
            "Decision Making",
            "Perform Stakeholder Analysis",
            "Recommend Actions for Improvement"
        ],
        "respuesta": "Plan Traceability Approach",
        "explicacion": "Elements include Organization of Business Analysis Information, Level of Abstraction, Plan Traceability Approach, Plan for Requirements Reuse, Storage and Access, and Requirements Attributes.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Traceability is best described as:",
        "opciones": [
            "The ability to track relationships among requirements, designs, and other items",
            "The process of approving requirements",
            "The storage location of documents",
            "The technique for prioritizing requirements"
        ],
        "respuesta": "The ability to track relationships among requirements, designs, and other items",
        "explicacion": "Traceability links requirements to their sources, to one another, and to designs and solution components, supporting impact analysis and coverage.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "The 'Level of Abstraction' element addresses:",
        "opciones": [
            "The appropriate level of detail for representing information to different audiences",
            "Where the information is stored",
            "Who approves the requirements",
            "How performance is measured"
        ],
        "respuesta": "The appropriate level of detail for representing information to different audiences",
        "explicacion": "Level of Abstraction concerns how detailed or high-level the information should be, varying by audience and purpose.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which element concerns how information will be structured and labeled so it can be located and used?",
        "opciones": [
            "Organization of Business Analysis Information",
            "Plan for Requirements Reuse",
            "Requirements Attributes",
            "Storage and Access"
        ],
        "respuesta": "Organization of Business Analysis Information",
        "explicacion": "Organization of Business Analysis Information defines how information is structured so relationships are clear and items can be found and used.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Requirements attributes are:",
        "opciones": [
            "Metadata describing requirements, such as priority, source, status, and owner",
            "The requirements themselves",
            "Approval signatures",
            "The storage tool's settings"
        ],
        "respuesta": "Metadata describing requirements, such as priority, source, status, and owner",
        "explicacion": "Requirements attributes are metadata (e.g., priority, source, status, owner, complexity) that support management and traceability of requirements.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which of the following is an example of a requirements attribute?",
        "opciones": [
            "Priority",
            "The change control board",
            "The onion diagram",
            "The RACI matrix"
        ],
        "respuesta": "Priority",
        "explicacion": "Priority is a common requirements attribute. Other examples include source, status, owner, complexity, and stability.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "The 'Plan for Requirements Reuse' element focuses on:",
        "opciones": [
            "Identifying requirements that can be used again in current or future initiatives",
            "Deleting old requirements",
            "Approving requirements",
            "Prioritizing requirements"
        ],
        "respuesta": "Identifying requirements that can be used again in current or future initiatives",
        "explicacion": "Plan for Requirements Reuse identifies requirements worth retaining and structuring so they can be reused later, saving effort.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which requirements are typically the best candidates for reuse?",
        "opciones": [
            "Stable, ongoing requirements such as regulatory rules and standard processes",
            "Highly volatile, one-off requirements",
            "Requirements that have been rejected",
            "Requirements with no owner"
        ],
        "respuesta": "Stable, ongoing requirements such as regulatory rules and standard processes",
        "explicacion": "Stable, enduring requirements (e.g., compliance rules, standard business processes) are the most valuable to retain for reuse.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "The 'Storage and Access' element determines:",
        "opciones": [
            "Where business analysis information is kept and how stakeholders can access it",
            "Who approves requirements",
            "How requirements are prioritized",
            "Which stakeholders to engage"
        ],
        "respuesta": "Where business analysis information is kept and how stakeholders can access it",
        "explicacion": "Storage and Access addresses how and where information is stored and how stakeholders retrieve and use it (tools, repositories, permissions).",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Why is the Governance Approach an input to information management planning?",
        "opciones": [
            "Governance decisions (e.g., approvals and changes) affect what information must be tracked and how",
            "Governance stores all requirements physically",
            "Governance replaces the need for traceability",
            "Governance is unrelated to information"
        ],
        "respuesta": "Governance decisions (e.g., approvals and changes) affect what information must be tracked and how",
        "explicacion": "Because governance defines approvals and change control, it influences which attributes, traceability, and records the information management approach must support.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "A key benefit of traceability is:",
        "opciones": [
            "Supporting impact analysis when a requirement changes",
            "Eliminating the need for approvals",
            "Removing stakeholders from the project",
            "Avoiding documentation"
        ],
        "respuesta": "Supporting impact analysis when a requirement changes",
        "explicacion": "Traceability enables impact analysis by showing which items are affected when a requirement or design changes, and confirms coverage.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Why is the Stakeholder Engagement Approach an input to information management planning?",
        "opciones": [
            "Stakeholders' information needs and access requirements shape how information is managed",
            "It stores the requirements repository",
            "It approves all requirements",
            "It is irrelevant to information"
        ],
        "respuesta": "Stakeholders' information needs and access requirements shape how information is managed",
        "explicacion": "Knowing stakeholders' communication and access needs helps determine how information should be organized, stored, and shared.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Item Tracking supports information management by:",
        "opciones": [
            "Recording and managing issues, risks, and other items along with their attributes",
            "Approving requirements",
            "Prioritizing the backlog",
            "Identifying stakeholders"
        ],
        "respuesta": "Recording and managing issues, risks, and other items along with their attributes",
        "explicacion": "Item Tracking captures items and their attributes and status, contributing to organized, accessible business analysis information.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Mind Mapping can support information management planning by:",
        "opciones": [
            "Helping to organize and structure business analysis information visually",
            "Approving the requirements baseline",
            "Defining the change control board",
            "Computing ROI"
        ],
        "respuesta": "Helping to organize and structure business analysis information visually",
        "explicacion": "Mind Mapping can help structure and relate pieces of business analysis information, aiding organization decisions.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "The appropriate level of abstraction for a deliverable depends primarily on:",
        "opciones": [
            "The audience and the purpose of the information",
            "The storage tool only",
            "The number of stakeholders only",
            "The project budget only"
        ],
        "respuesta": "The audience and the purpose of the information",
        "explicacion": "Executives may need high-level summaries while developers need detailed specifications; abstraction is chosen by audience and purpose.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "A traceability matrix is most directly used to:",
        "opciones": [
            "Show the links between requirements and other items",
            "Prioritize requirements by value",
            "Identify stakeholders",
            "Approve the solution scope"
        ],
        "respuesta": "Show the links between requirements and other items",
        "explicacion": "A traceability matrix documents relationships between requirements and their sources, designs, tests, or other requirements.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which of the following best describes 'requirements reuse' value?",
        "opciones": [
            "It reduces effort and improves consistency across initiatives",
            "It guarantees zero defects",
            "It removes the need for elicitation forever",
            "It eliminates the need for stakeholders"
        ],
        "respuesta": "It reduces effort and improves consistency across initiatives",
        "explicacion": "Reuse saves analysis effort and promotes consistency by leveraging previously defined, validated requirements.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which factor most influences how formal and detailed the information management approach should be?",
        "opciones": [
            "The complexity of the change and organizational/regulatory requirements",
            "The color of the requirements tool",
            "The number of meeting rooms available",
            "The brand of laptops used"
        ],
        "respuesta": "The complexity of the change and organizational/regulatory requirements",
        "explicacion": "Information management formality scales with the complexity of the change and any organizational or regulatory requirements.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Storage and access decisions should consider:",
        "opciones": [
            "Tools, access permissions, security, and how information will be retrieved",
            "Only the document font",
            "Only the sponsor's email address",
            "Only the prioritization criteria"
        ],
        "respuesta": "Tools, access permissions, security, and how information will be retrieved",
        "explicacion": "Storage and access covers the repository or tools, who can access information, security needs, and retrieval methods.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Interviews support information management planning by:",
        "opciones": [
            "Eliciting stakeholders' needs for accessing and using business analysis information",
            "Approving the information management approach",
            "Storing the repository",
            "Prioritizing requirements automatically"
        ],
        "respuesta": "Eliciting stakeholders' needs for accessing and using business analysis information",
        "explicacion": "Interviews gather stakeholder input on what information they need and how they prefer to access it.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "In an adaptive context, the information management approach tends to favor:",
        "opciones": [
            "Lighter, just-enough documentation managed in accessible tools",
            "Heavy formal documentation approved in advance",
            "No information management at all",
            "Storage decided by the regulator only"
        ],
        "respuesta": "Lighter, just-enough documentation managed in accessible tools",
        "explicacion": "Adaptive contexts favor lightweight, just-enough information captured in accessible, collaborative tools.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which is TRUE about the relationship between attributes and traceability?",
        "opciones": [
            "Well-defined attributes can support and enrich traceability information",
            "Attributes and traceability are unrelated",
            "Attributes replace the need for traceability",
            "Traceability prevents the use of attributes"
        ],
        "respuesta": "Well-defined attributes can support and enrich traceability information",
        "explicacion": "Attributes such as source and status complement traceability links, together giving a fuller picture of each requirement.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Lessons Learned contributes to information management planning by:",
        "opciones": [
            "Drawing on past experience to choose effective organization, storage, and reuse practices",
            "Approving the requirements",
            "Defining stakeholder personas",
            "Calculating financial value"
        ],
        "respuesta": "Drawing on past experience to choose effective organization, storage, and reuse practices",
        "explicacion": "Lessons Learned applies insights from previous initiatives to improve how information is organized, stored, and reused.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which of the following is a common requirements attribute used to indicate where a requirement came from?",
        "opciones": [
            "Source",
            "Onion ring",
            "RACI letter",
            "Sprint velocity"
        ],
        "respuesta": "Source",
        "explicacion": "Source identifies the origin of a requirement (stakeholder, document, regulation), which supports validation and traceability.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "The 'status' attribute of a requirement might take values such as:",
        "opciones": [
            "Proposed, approved, implemented, verified",
            "High, medium, low priority only",
            "Red, green, blue",
            "Predictive, adaptive, hybrid"
        ],
        "respuesta": "Proposed, approved, implemented, verified",
        "explicacion": "Status tracks the lifecycle stage of a requirement, such as proposed, approved, implemented, or verified.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Process Modelling supports information management planning by:",
        "opciones": [
            "Documenting how business analysis information will flow and be managed",
            "Approving the requirements",
            "Identifying the regulator",
            "Computing risk scores"
        ],
        "respuesta": "Documenting how business analysis information will flow and be managed",
        "explicacion": "Process Modelling can depict how information is created, reviewed, stored, and accessed throughout the initiative.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Why is the Business Analysis Approach an input to this task?",
        "opciones": [
            "It influences the type, formality, and volume of information to be managed",
            "It physically stores the information",
            "It approves all changes",
            "It selects the regulator"
        ],
        "respuesta": "It influences the type, formality, and volume of information to be managed",
        "explicacion": "The Business Analysis Approach determines what deliverables exist and how formal they are, shaping the information management approach.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which best describes the value of organizing business analysis information well?",
        "opciones": [
            "Stakeholders can find, understand, and use the information efficiently",
            "It guarantees the project is on budget",
            "It removes the need for governance",
            "It eliminates change requests"
        ],
        "respuesta": "Stakeholders can find, understand, and use the information efficiently",
        "explicacion": "Good organization makes information accessible, understandable, and usable, supporting effective decisions and collaboration.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "A decision about how long business analysis information should be retained falls under:",
        "opciones": [
            "Storage and Access (and reuse considerations)",
            "Decision Making",
            "Perform Stakeholder Analysis",
            "Assessment Measures"
        ],
        "respuesta": "Storage and Access (and reuse considerations)",
        "explicacion": "Retention is part of how information is stored and accessed, and connects to reuse decisions about which information to keep.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Traceability that links requirements 'backward' to their origin supports:",
        "opciones": [
            "Verifying that each requirement is justified by a need or source",
            "Prioritizing the backlog",
            "Identifying the sponsor",
            "Selecting the methodology"
        ],
        "respuesta": "Verifying that each requirement is justified by a need or source",
        "explicacion": "Backward traceability links requirements to their origins, helping confirm each is justified and removing orphan requirements.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Traceability that links requirements 'forward' to designs and solution components supports:",
        "opciones": [
            "Confirming that requirements are covered by the solution",
            "Identifying stakeholders",
            "Choosing a regulator",
            "Defining personas"
        ],
        "respuesta": "Confirming that requirements are covered by the solution",
        "explicacion": "Forward traceability confirms coverage—that each requirement is addressed by designs, components, and tests.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "The decision about which requirements attributes to capture should be based on:",
        "opciones": [
            "The information needed to manage and trace requirements for the initiative",
            "Capturing every conceivable attribute regardless of value",
            "Only the sponsor's preference for colors",
            "The number of developers"
        ],
        "respuesta": "The information needed to manage and trace requirements for the initiative",
        "explicacion": "Attributes are chosen to support effective management and traceability without unnecessary overhead; only useful attributes should be captured.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Brainstorming supports information management planning by:",
        "opciones": [
            "Generating ideas about how to organize, store, and reuse information",
            "Approving the requirements baseline",
            "Defining decision authority",
            "Calculating ROI"
        ],
        "respuesta": "Generating ideas about how to organize, store, and reuse information",
        "explicacion": "Brainstorming generates options for organizing, storing, and reusing business analysis information.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which is the BEST reason to plan requirements reuse during information management planning?",
        "opciones": [
            "To structure and store requirements so they can be efficiently retrieved and reused later",
            "To delete requirements after use",
            "To avoid documenting requirements",
            "To prevent stakeholders from seeing requirements"
        ],
        "respuesta": "To structure and store requirements so they can be efficiently retrieved and reused later",
        "explicacion": "Planning reuse means structuring and storing requirements (e.g., at the right abstraction) so future initiatives can find and reuse them.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Surveys or questionnaires support this task by:",
        "opciones": [
            "Collecting stakeholders' information access and format preferences at scale",
            "Approving the information management approach",
            "Storing the repository",
            "Prioritizing requirements automatically"
        ],
        "respuesta": "Collecting stakeholders' information access and format preferences at scale",
        "explicacion": "Surveys gather information needs and preferences from many stakeholders, informing storage, access, and format decisions.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which of the following is NOT an element of Plan Business Analysis Information Management?",
        "opciones": [
            "Plan Prioritization Approach",
            "Plan Traceability Approach",
            "Storage and Access",
            "Requirements Attributes"
        ],
        "respuesta": "Plan Prioritization Approach",
        "explicacion": "Plan Prioritization Approach belongs to Plan Business Analysis Governance, not to information management.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "How does the level of abstraction relate to different stakeholders?",
        "opciones": [
            "Different stakeholders need information at different levels of detail",
            "All stakeholders need identical detail",
            "Only the sponsor needs any information",
            "Abstraction applies only to developers"
        ],
        "respuesta": "Different stakeholders need information at different levels of detail",
        "explicacion": "Abstraction is tailored so each stakeholder receives the appropriate level of detail for their role and decisions.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "An 'owner' attribute on a requirement indicates:",
        "opciones": [
            "The stakeholder responsible for the requirement",
            "The storage server name",
            "The methodology used",
            "The priority level"
        ],
        "respuesta": "The stakeholder responsible for the requirement",
        "explicacion": "The owner attribute identifies the stakeholder accountable for or responsible for a given requirement.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Workshops support information management planning by:",
        "opciones": [
            "Collaboratively agreeing on how information will be organized, stored, and accessed",
            "Approving the solution",
            "Storing the requirements repository physically",
            "Calculating financial returns"
        ],
        "respuesta": "Collaboratively agreeing on how information will be organized, stored, and accessed",
        "explicacion": "Workshops gather stakeholders to agree on organization, storage, access, and reuse approaches.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which statement about the Information Management Approach is TRUE?",
        "opciones": [
            "It should be consistent with the governance and engagement approaches",
            "It is independent of all other approaches",
            "It replaces the governance approach",
            "It is only relevant after the project ends"
        ],
        "respuesta": "It should be consistent with the governance and engagement approaches",
        "explicacion": "Since governance and engagement approaches are inputs, the information management approach must be consistent with them.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "A 'complexity' attribute on a requirement helps with:",
        "opciones": [
            "Estimation and prioritization decisions",
            "Choosing the regulator",
            "Selecting the meeting room",
            "Defining stakeholder personas"
        ],
        "respuesta": "Estimation and prioritization decisions",
        "explicacion": "A complexity attribute aids estimation of effort and informs prioritization and sequencing decisions.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "When a requirement changes, traceability allows the business analyst to:",
        "opciones": [
            "Quickly identify all related items that may also need to change",
            "Automatically approve the change",
            "Avoid notifying stakeholders",
            "Delete the requirement permanently"
        ],
        "respuesta": "Quickly identify all related items that may also need to change",
        "explicacion": "Traceability enables impact analysis by revealing related requirements, designs, and components affected by a change.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "The decision about traceability formality should consider:",
        "opciones": [
            "The complexity, risk, and reuse needs of the initiative versus the effort to maintain it",
            "Only the sponsor's job title",
            "The font of the requirements document",
            "The number of office floors"
        ],
        "respuesta": "The complexity, risk, and reuse needs of the initiative versus the effort to maintain it",
        "explicacion": "Traceability formality is balanced against the value it provides (for complexity, risk, reuse) and the cost to create and maintain it.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which is an example of business analysis information that may be managed under this task?",
        "opciones": [
            "Requirements, designs, models, and elicitation results",
            "The company's payroll only",
            "The office cleaning schedule",
            "Marketing brochures only"
        ],
        "respuesta": "Requirements, designs, models, and elicitation results",
        "explicacion": "Business analysis information includes requirements, designs, models, diagrams, and elicitation results produced during the work.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Why might an organization standardize the storage tool for business analysis information?",
        "opciones": [
            "To improve consistency, accessibility, and reuse across initiatives",
            "To prevent stakeholders from accessing information",
            "To eliminate the need for requirements",
            "To avoid traceability"
        ],
        "respuesta": "To improve consistency, accessibility, and reuse across initiatives",
        "explicacion": "Standard tooling improves consistency, makes information easier to access, and supports reuse across multiple initiatives.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which statement best captures the overall goal of this task?",
        "opciones": [
            "To ensure business analysis information is well managed and available to those who need it",
            "To approve the final solution",
            "To eliminate all stakeholders",
            "To measure team velocity"
        ],
        "respuesta": "To ensure business analysis information is well managed and available to those who need it",
        "explicacion": "The task ensures information is organized, traceable, stored, accessible, and reusable so it serves stakeholders effectively.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    # ============================================================
    # 3.5 IDENTIFY BUSINESS ANALYSIS PERFORMANCE IMPROVEMENTS (Q201-Q250)
    # ============================================================
    {
        "pregunta": "What is the purpose of the Identify Business Analysis Performance Improvements task?",
        "opciones": [
            "To assess business analysis work and plan to improve processes where required",
            "To store business analysis information",
            "To approve requirements and designs",
            "To identify stakeholders"
        ],
        "respuesta": "To assess business analysis work and plan to improve processes where required",
        "explicacion": "This task assesses how business analysis work is performed and identifies actions to improve it.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which is the output of the Identify Business Analysis Performance Improvements task?",
        "opciones": [
            "Business Analysis Performance Assessment",
            "Governance Approach",
            "Information Management Approach",
            "Stakeholder Engagement Approach"
        ],
        "respuesta": "Business Analysis Performance Assessment",
        "explicacion": "The output is the Business Analysis Performance Assessment, which includes the assessment of performance and recommended improvement actions.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which are the inputs to this task?",
        "opciones": [
            "Business Analysis Approach and Performance Objectives",
            "Needs only",
            "Governance Approach only",
            "Requirements and Designs"
        ],
        "respuesta": "Business Analysis Approach and Performance Objectives",
        "explicacion": "Inputs are the Business Analysis Approach and Performance Objectives (external), against which performance is assessed.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which of the following is an element of this task?",
        "opciones": [
            "Performance Analysis",
            "Plan Traceability Approach",
            "Change Control Process",
            "Perform Stakeholder Analysis"
        ],
        "respuesta": "Performance Analysis",
        "explicacion": "Elements are Performance Analysis, Assessment Measures, Analyze Results, and Recommend Actions for Improvement.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "The 'Assessment Measures' element involves:",
        "opciones": [
            "Determining the measures used to evaluate business analysis performance",
            "Approving requirements",
            "Storing requirements",
            "Identifying stakeholders"
        ],
        "respuesta": "Determining the measures used to evaluate business analysis performance",
        "explicacion": "Assessment Measures defines the metrics and measures—such as accuracy, timeliness, and stakeholder satisfaction—used to evaluate performance.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Performance measures for business analysis work may include:",
        "opciones": [
            "Accuracy and completeness, timeliness, and stakeholder satisfaction",
            "The brand of the requirements tool",
            "The number of office chairs",
            "The color of status reports"
        ],
        "respuesta": "Accuracy and completeness, timeliness, and stakeholder satisfaction",
        "explicacion": "Common measures include accuracy/completeness of deliverables, knowledge, effectiveness, timeliness, and stakeholder satisfaction.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Performance measures can be qualitative or quantitative. An example of a qualitative measure is:",
        "opciones": [
            "Stakeholder satisfaction with deliverables",
            "Number of requirements changed",
            "Hours spent on elicitation",
            "Count of defects found"
        ],
        "respuesta": "Stakeholder satisfaction with deliverables",
        "explicacion": "Stakeholder satisfaction is a qualitative measure, whereas counts and durations are quantitative measures.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Root Cause Analysis is used in this task to:",
        "opciones": [
            "Identify the underlying causes of performance problems",
            "Approve the requirements baseline",
            "Store performance data",
            "Identify all stakeholders"
        ],
        "respuesta": "Identify the underlying causes of performance problems",
        "explicacion": "Root Cause Analysis investigates the underlying reasons for performance issues so that improvements address causes, not just symptoms.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "The 'Analyze Results' element involves:",
        "opciones": [
            "Comparing actual performance against measures to identify problems and opportunities",
            "Approving the requirements",
            "Selecting the storage tool",
            "Creating the stakeholder list"
        ],
        "respuesta": "Comparing actual performance against measures to identify problems and opportunities",
        "explicacion": "Analyze Results compares performance against the chosen measures and objectives to surface problems, gaps, and improvement opportunities.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "The 'Recommend Actions for Improvement' element results in:",
        "opciones": [
            "Recommendations to improve business analysis performance",
            "Approval of the solution",
            "A stakeholder map",
            "A change control board"
        ],
        "respuesta": "Recommendations to improve business analysis performance",
        "explicacion": "This element produces actionable recommendations to improve how business analysis work is performed.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Why are Performance Objectives an input to this task?",
        "opciones": [
            "They provide the targets against which business analysis performance is assessed",
            "They store the requirements",
            "They identify the regulator",
            "They approve all changes"
        ],
        "respuesta": "They provide the targets against which business analysis performance is assessed",
        "explicacion": "Performance Objectives (often set externally by the organization) are the benchmarks used to evaluate whether performance is acceptable.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which technique uses metrics and KPIs to track and assess business analysis performance?",
        "opciones": [
            "Metrics and Key Performance Indicators",
            "Scope Modelling",
            "Data Modelling",
            "Concept Modelling"
        ],
        "respuesta": "Metrics and Key Performance Indicators",
        "explicacion": "Metrics and KPIs define and track measurable indicators of business analysis performance against objectives.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Observation can be used in this task to:",
        "opciones": [
            "Directly watch business analysis activities to assess performance",
            "Approve requirements",
            "Store performance data",
            "Define stakeholder personas"
        ],
        "respuesta": "Directly watch business analysis activities to assess performance",
        "explicacion": "Observation involves watching the work being performed to gather firsthand information about performance.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Process Analysis is used in this task to:",
        "opciones": [
            "Examine the business analysis process to find inefficiencies and improvement opportunities",
            "Approve requirements",
            "Identify stakeholders",
            "Store information"
        ],
        "respuesta": "Examine the business analysis process to find inefficiencies and improvement opportunities",
        "explicacion": "Process Analysis evaluates the current business analysis process to identify waste, bottlenecks, and opportunities to improve.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which technique captures insights at the end of, or during, work for future improvement?",
        "opciones": [
            "Lessons Learned",
            "Data Modelling",
            "Interface Analysis",
            "Glossary"
        ],
        "respuesta": "Lessons Learned",
        "explicacion": "Lessons Learned gathers what went well and what could improve, feeding the performance assessment and future work.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "The Business Analysis Performance Assessment is also used as a guideline or tool in which task?",
        "opciones": [
            "Plan Business Analysis Approach",
            "Plan Stakeholder Engagement",
            "Plan Business Analysis Information Management",
            "Define Solution Scope"
        ],
        "respuesta": "Plan Business Analysis Approach",
        "explicacion": "The Business Analysis Performance Assessment informs Plan Business Analysis Approach, helping plan a more effective approach based on past performance.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "The 'Performance Analysis' element focuses on:",
        "opciones": [
            "Reviewing reports and other information to understand business analysis performance",
            "Approving the requirements baseline",
            "Storing the information repository",
            "Identifying stakeholders' attitudes"
        ],
        "respuesta": "Reviewing reports and other information to understand business analysis performance",
        "explicacion": "Performance Analysis reviews available reports and information to understand and characterize current business analysis performance.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which stakeholder commonly provides feedback on the quality and timeliness of business analysis deliverables?",
        "opciones": [
            "Any stakeholder who receives or uses the deliverables",
            "Only the regulator",
            "Only external auditors",
            "No stakeholders provide feedback"
        ],
        "respuesta": "Any stakeholder who receives or uses the deliverables",
        "explicacion": "Stakeholders who use business analysis deliverables can provide valuable feedback on their quality, usefulness, and timeliness.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Performance measures should ideally be agreed:",
        "opciones": [
            "With relevant stakeholders, so the assessment is meaningful and accepted",
            "Secretly by the business analyst alone",
            "Only after the project ends",
            "By the development team without input"
        ],
        "respuesta": "With relevant stakeholders, so the assessment is meaningful and accepted",
        "explicacion": "Agreeing measures with stakeholders ensures the assessment is relevant, fair, and accepted by those involved.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "A recommendation for improvement might include:",
        "opciones": [
            "Adopting a new technique or adjusting the approach for future work",
            "Deleting all requirements",
            "Removing the sponsor",
            "Ignoring stakeholder feedback"
        ],
        "respuesta": "Adopting a new technique or adjusting the approach for future work",
        "explicacion": "Improvement recommendations can include process changes, new techniques, training, or adjustments to the approach.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Interviews support this task by:",
        "opciones": [
            "Gathering stakeholder perceptions of business analysis performance",
            "Approving the requirements",
            "Storing performance metrics",
            "Defining the prioritization scheme"
        ],
        "respuesta": "Gathering stakeholder perceptions of business analysis performance",
        "explicacion": "Interviews collect stakeholders' views on how well business analysis work was performed and where it could improve.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Surveys or questionnaires in this task are useful for:",
        "opciones": [
            "Collecting performance feedback from many stakeholders efficiently",
            "Approving the performance assessment",
            "Storing the metrics",
            "Identifying the regulator"
        ],
        "respuesta": "Collecting performance feedback from many stakeholders efficiently",
        "explicacion": "Surveys efficiently gather performance feedback (e.g., satisfaction) from a large group of stakeholders.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Why should performance improvement be an ongoing activity?",
        "opciones": [
            "Continuous assessment allows timely correction and steady improvement of business analysis work",
            "It is only relevant after a project fails",
            "It replaces the need for governance",
            "It is required only by regulators"
        ],
        "respuesta": "Continuous assessment allows timely correction and steady improvement of business analysis work",
        "explicacion": "Ongoing assessment lets the team correct issues promptly and continuously improve rather than waiting until the end.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Item Tracking supports this task by:",
        "opciones": [
            "Recording performance-related issues and tracking improvement actions to closure",
            "Approving requirements",
            "Defining stakeholder personas",
            "Calculating ROI"
        ],
        "respuesta": "Recording performance-related issues and tracking improvement actions to closure",
        "explicacion": "Item Tracking logs performance issues and follows improvement actions through to resolution.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Reviews are used in this task to:",
        "opciones": [
            "Evaluate business analysis work products and processes for quality and improvement",
            "Approve the solution scope",
            "Store the metrics",
            "Identify stakeholders"
        ],
        "respuesta": "Evaluate business analysis work products and processes for quality and improvement",
        "explicacion": "Reviews assess work products and processes, surfacing quality issues and improvement opportunities.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which best describes a good performance measure?",
        "opciones": [
            "Relevant, measurable, and tied to performance objectives",
            "Vague and subjective with no link to objectives",
            "Impossible to measure",
            "Unrelated to business analysis work"
        ],
        "respuesta": "Relevant, measurable, and tied to performance objectives",
        "explicacion": "Effective measures are relevant, measurable, and aligned to the performance objectives being assessed.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Risk Analysis and Management can support this task by:",
        "opciones": [
            "Identifying risks to business analysis performance and planning mitigations",
            "Approving requirements",
            "Storing the performance assessment",
            "Defining the onion diagram"
        ],
        "respuesta": "Identifying risks to business analysis performance and planning mitigations",
        "explicacion": "Risk Analysis and Management can highlight risks that threaten performance and inform mitigation as part of improvement.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "If deliverables are consistently late, an appropriate first step in this task is to:",
        "opciones": [
            "Analyze the root causes of the lateness before recommending actions",
            "Immediately fire the team",
            "Ignore the issue",
            "Delete the deliverables"
        ],
        "respuesta": "Analyze the root causes of the lateness before recommending actions",
        "explicacion": "Understanding root causes ensures recommendations address the real reasons for poor performance rather than symptoms.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Workshops support this task by:",
        "opciones": [
            "Bringing stakeholders together to assess performance and agree on improvements",
            "Approving the requirements",
            "Storing performance data",
            "Identifying the regulator"
        ],
        "respuesta": "Bringing stakeholders together to assess performance and agree on improvements",
        "explicacion": "Workshops gather stakeholders to collaboratively evaluate performance and define improvement actions (e.g., retrospectives).",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Process Modelling supports this task by:",
        "opciones": [
            "Documenting the current and improved business analysis processes",
            "Approving the solution",
            "Identifying stakeholders only",
            "Calculating financial returns"
        ],
        "respuesta": "Documenting the current and improved business analysis processes",
        "explicacion": "Process Modelling depicts the existing process and proposed improvements, supporting analysis and communication of changes.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which is an example of a quantitative performance measure?",
        "opciones": [
            "Number of requirements defects found after sign-off",
            "Stakeholder feeling about collaboration",
            "Perceived clarity of documents",
            "General morale"
        ],
        "respuesta": "Number of requirements defects found after sign-off",
        "explicacion": "Defect counts are quantitative measures, while perceptions and feelings are qualitative.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Performance Objectives often originate from:",
        "opciones": [
            "The organization and its broader performance management context",
            "The development team's daily standup",
            "The requirements repository",
            "The change control board minutes"
        ],
        "respuesta": "The organization and its broader performance management context",
        "explicacion": "Performance Objectives commonly come from the organization, reflecting its goals and performance management practices.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which is the BEST description of the relationship between this task and the Business Analysis Approach?",
        "opciones": [
            "The approach defines how work is done; this task assesses how well it was done and recommends improvements",
            "They are identical tasks",
            "The approach replaces this task",
            "This task approves the approach"
        ],
        "respuesta": "The approach defines how work is done; this task assesses how well it was done and recommends improvements",
        "explicacion": "The Business Analysis Approach (an input) defines the planned way of working; this task evaluates performance against it and suggests improvements.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Brainstorming supports this task by:",
        "opciones": [
            "Generating ideas for performance measures and possible improvements",
            "Approving requirements",
            "Storing the metrics",
            "Selecting the regulator"
        ],
        "respuesta": "Generating ideas for performance measures and possible improvements",
        "explicacion": "Brainstorming generates candidate performance measures and improvement ideas with the team and stakeholders.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "A retrospective at the end of an iteration is most aligned with which task?",
        "opciones": [
            "Identify Business Analysis Performance Improvements",
            "Plan Stakeholder Engagement",
            "Plan Business Analysis Governance",
            "Plan Business Analysis Information Management"
        ],
        "respuesta": "Identify Business Analysis Performance Improvements",
        "explicacion": "Retrospectives review how work was performed and identify improvements, aligning with this task in adaptive contexts.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "The frequency of performance assessment should be:",
        "opciones": [
            "Appropriate to the initiative—e.g., per iteration in adaptive work or at milestones in predictive work",
            "Only once, at project closure, in all cases",
            "Never, to save time",
            "Decided solely by the regulator"
        ],
        "respuesta": "Appropriate to the initiative—e.g., per iteration in adaptive work or at milestones in predictive work",
        "explicacion": "Assessment cadence is tailored to the initiative; adaptive work assesses frequently (each iteration) while predictive work may assess at milestones.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "When recommending improvements, the business analyst should consider:",
        "opciones": [
            "The cost, feasibility, and expected benefit of each recommendation",
            "Only the most expensive options",
            "Only changes the regulator demands",
            "Recommendations should not be evaluated"
        ],
        "respuesta": "The cost, feasibility, and expected benefit of each recommendation",
        "explicacion": "Recommendations are weighed by feasibility, cost, and benefit so that improvements are worthwhile and practical.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which of the following is NOT an element of this task?",
        "opciones": [
            "Plan for Approvals",
            "Performance Analysis",
            "Assessment Measures",
            "Recommend Actions for Improvement"
        ],
        "respuesta": "Plan for Approvals",
        "explicacion": "Plan for Approvals belongs to Plan Business Analysis Governance, not to this task.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "How does stakeholder satisfaction serve as a performance measure?",
        "opciones": [
            "It indicates how well business analysis work met stakeholder needs and expectations",
            "It measures the project's profit",
            "It counts the number of stakeholders",
            "It has no value as a measure"
        ],
        "respuesta": "It indicates how well business analysis work met stakeholder needs and expectations",
        "explicacion": "Stakeholder satisfaction reflects whether the work met expectations, signaling the effectiveness of business analysis.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which is the BEST reason to document the performance assessment?",
        "opciones": [
            "To provide a record that informs future planning and demonstrates improvement over time",
            "To delete it immediately after creation",
            "To hide it from stakeholders",
            "To replace the requirements documentation"
        ],
        "respuesta": "To provide a record that informs future planning and demonstrates improvement over time",
        "explicacion": "Documenting the assessment creates a reusable record that informs future approaches and shows improvement trends.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "A measure of 'timeliness' for business analysis deliverables would track:",
        "opciones": [
            "Whether deliverables were produced on schedule",
            "The color of the deliverables",
            "The number of stakeholders",
            "The storage tool used"
        ],
        "respuesta": "Whether deliverables were produced on schedule",
        "explicacion": "Timeliness measures whether business analysis deliverables were completed within expected timeframes.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which best describes the link between Analyze Results and Recommend Actions for Improvement?",
        "opciones": [
            "Analysis reveals problems and opportunities, which drive specific improvement recommendations",
            "They are unrelated steps",
            "Recommendations come before any analysis",
            "Analysis replaces the need for recommendations"
        ],
        "respuesta": "Analysis reveals problems and opportunities, which drive specific improvement recommendations",
        "explicacion": "Analyzing results identifies issues and opportunities, which then inform targeted recommendations for improvement.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "If a performance measure shows requirements are frequently misunderstood, a likely improvement is:",
        "opciones": [
            "Improving elicitation or the clarity and review of requirements",
            "Removing all requirements",
            "Stopping stakeholder engagement",
            "Eliminating the sponsor role"
        ],
        "respuesta": "Improving elicitation or the clarity and review of requirements",
        "explicacion": "Frequent misunderstanding suggests improving how requirements are elicited, expressed, and reviewed for clarity.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which statement about who performs the performance assessment is most accurate?",
        "opciones": [
            "It can be performed by the business analyst with input from relevant stakeholders",
            "Only external auditors can perform it",
            "Only the regulator can perform it",
            "It cannot be performed by the business analyst"
        ],
        "respuesta": "It can be performed by the business analyst with input from relevant stakeholders",
        "explicacion": "The business analyst typically conducts the assessment, gathering input and feedback from stakeholders involved in or affected by the work.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Why is it important to tie performance measures to objectives rather than measuring everything?",
        "opciones": [
            "To focus on what matters and avoid wasted effort on irrelevant metrics",
            "Because measuring everything is always free",
            "Because objectives are unrelated to performance",
            "To prevent any measurement at all"
        ],
        "respuesta": "To focus on what matters and avoid wasted effort on irrelevant metrics",
        "explicacion": "Aligning measures to objectives keeps the assessment focused and meaningful, avoiding effort on metrics that do not matter.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "An improvement recommendation that addresses a root cause rather than a symptom is preferable because:",
        "opciones": [
            "It is more likely to prevent the problem from recurring",
            "It is always cheaper",
            "Symptoms never matter",
            "Root causes are easier to ignore"
        ],
        "respuesta": "It is more likely to prevent the problem from recurring",
        "explicacion": "Addressing root causes prevents recurrence, whereas treating symptoms often allows the problem to return.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which of the following best summarizes the value of this task to the organization?",
        "opciones": [
            "It helps business analysis work become more effective and efficient over time",
            "It guarantees the project will never change",
            "It removes the need for stakeholders",
            "It replaces all other planning tasks"
        ],
        "respuesta": "It helps business analysis work become more effective and efficient over time",
        "explicacion": "By assessing performance and recommending improvements, the task drives ongoing gains in the effectiveness and efficiency of business analysis.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "The Business Analysis Performance Assessment typically includes:",
        "opciones": [
            "An assessment of performance plus recommended actions for improvement",
            "Only the project budget",
            "Only the stakeholder list",
            "Only the change log"
        ],
        "respuesta": "An assessment of performance plus recommended actions for improvement",
        "explicacion": "The assessment documents how performance compared to measures/objectives and provides recommended improvement actions.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "Which best describes why stakeholder personas are useful when planning engagement?",
        "opciones": [
            "They summarize the goals and characteristics of a stakeholder group to guide engagement decisions",
            "They formally approve requirements",
            "They store the requirements repository",
            "They calculate the project budget"
        ],
        "respuesta": "They summarize the goals and characteristics of a stakeholder group to guide engagement decisions",
        "explicacion": "Personas capture representative goals, needs, and behaviors of a stakeholder group, helping tailor how that group is engaged.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "A stakeholder with low power and low interest is typically engaged by:",
        "opciones": [
            "Monitoring with minimal effort",
            "Daily one-on-one meetings",
            "Granting full approval authority",
            "Excluding them from the stakeholder list permanently"
        ],
        "respuesta": "Monitoring with minimal effort",
        "explicacion": "Low-power, low-interest stakeholders are usually just monitored with minimal effort, escalating engagement only if their position changes.",
        "tarea": "3.2 Plan Stakeholder Engagement"
    },
    {
        "pregunta": "Which best explains why governance must define how requirements are prioritized?",
        "opciones": [
            "Limited time and resources mean not everything can be done at once, so decisions on sequence are needed",
            "Prioritization is forbidden by BABOK",
            "All requirements always have equal value",
            "Prioritization only matters after delivery"
        ],
        "respuesta": "Limited time and resources mean not everything can be done at once, so decisions on sequence are needed",
        "explicacion": "Because resources and time are constrained, governance establishes how requirements are prioritized so the most valuable work is done first.",
        "tarea": "3.3 Plan Business Analysis Governance"
    },
    {
        "pregunta": "Which best explains the purpose of capturing a 'stability' attribute for a requirement?",
        "opciones": [
            "It indicates how likely the requirement is to change, aiding planning and risk decisions",
            "It records the storage server location",
            "It identifies the regulator",
            "It approves the requirement"
        ],
        "respuesta": "It indicates how likely the requirement is to change, aiding planning and risk decisions",
        "explicacion": "A stability attribute signals how volatile a requirement is, informing sequencing, risk, and how much to invest in detailing it early.",
        "tarea": "3.4 Plan Business Analysis Information Management"
    },
    {
        "pregunta": "Which is the BEST example of an 'opportunity' (rather than a problem) found during performance analysis?",
        "opciones": [
            "A technique that worked well and could be applied more broadly",
            "Deliverables that were consistently late",
            "Requirements that were frequently misunderstood",
            "Stakeholders who were dissatisfied"
        ],
        "respuesta": "A technique that worked well and could be applied more broadly",
        "explicacion": "Performance analysis surfaces not only problems but also opportunities, such as a successful practice worth expanding.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
    {
        "pregunta": "When should baseline performance measures ideally be established?",
        "opciones": [
            "Early, so later performance can be compared against a meaningful reference",
            "Only after the initiative has completely failed",
            "Never, since measures are subjective",
            "Only by the regulator at audit time"
        ],
        "respuesta": "Early, so later performance can be compared against a meaningful reference",
        "explicacion": "Establishing baseline measures early provides a reference point so improvements or declines in performance can be detected and acted upon.",
        "tarea": "3.5 Identify Business Analysis Performance Improvements"
    },
]


# ==================================================================
# LÓGICA DEL SIMULADOR
# ==================================================================

TAREAS = [
    "All tasks",
    "3.1 Plan Business Analysis Approach",
    "3.2 Plan Stakeholder Engagement",
    "3.3 Plan Business Analysis Governance",
    "3.4 Plan Business Analysis Information Management",
    "3.5 Identify Business Analysis Performance Improvements",
]

# ---- Estado de sesión ----
def init_state():
    defaults = {
        "iniciado": False,
        "preguntas_sesion": [],
        "idx": 0,
        "aciertos": 0,
        "respondida": False,
        "seleccion": None,
        "historial": [],  # (idx_global, correcta_bool)
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ---- Encabezado ----
st.markdown('<div class="titulo">CBAP Exam Simulator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">BABOK&reg; v3 &mdash; Chapter 3: Business Analysis Planning and Monitoring</div>', unsafe_allow_html=True)

# ---- Pantalla de inicio ----
if not st.session_state.iniciado:
    st.markdown(f"**Total questions available:** {len(PREGUNTAS)}")

    tarea_sel = st.selectbox("Select task / knowledge area:", TAREAS, index=0)

    if tarea_sel == "All tasks":
        pool = list(PREGUNTAS)
    else:
        pool = [p for p in PREGUNTAS if p["tarea"] == tarea_sel]

    max_q = len(pool)
    num = st.slider("Number of questions in this session:",
                    min_value=1, max_value=max_q,
                    value=min(20, max_q))

    aleatorio = st.checkbox("Randomize question order", value=True)

    if st.button("Start simulator"):
        seleccion = list(pool)
        if aleatorio:
            random.shuffle(seleccion)
        st.session_state.preguntas_sesion = seleccion[:num]
        st.session_state.iniciado = True
        st.session_state.idx = 0
        st.session_state.aciertos = 0
        st.session_state.respondida = False
        st.session_state.seleccion = None
        st.session_state.historial = []
        st.rerun()

# ---- Pantalla de preguntas ----
else:
    sesion = st.session_state.preguntas_sesion
    total = len(sesion)
    idx = st.session_state.idx

    # ---- Pantalla de resultados final ----
    if idx >= total:
        aciertos = st.session_state.aciertos
        pct = (aciertos / total * 100) if total else 0
        st.markdown(f'<div class="titulo">Results</div>', unsafe_allow_html=True)
        if pct >= 70:
            st.markdown(
                f'<div class="correcto"><h3 style="color:#7fd18a;">Score: {aciertos}/{total} ({pct:.0f}%)</h3>'
                f'<p>Above the typical CBAP passing range. Great work!</p></div>',
                unsafe_allow_html=True)
        else:
            st.markdown(
                f'<div class="incorrecto"><h3 style="color:#e88;">Score: {aciertos}/{total} ({pct:.0f}%)</h3>'
                f'<p>Keep practicing &mdash; aim for ~70%+ before the exam.</p></div>',
                unsafe_allow_html=True)

        # Desglose por tarea
        from collections import defaultdict
        por_tarea = defaultdict(lambda: [0, 0])  # tarea -> [aciertos, total]
        for (gi, ok) in st.session_state.historial:
            t = sesion[gi]["tarea"]
            por_tarea[t][1] += 1
            if ok:
                por_tarea[t][0] += 1
        if por_tarea:
            st.markdown("#### Breakdown by task")
            for t, (a, tt) in por_tarea.items():
                st.markdown(f"- **{t}** &mdash; {a}/{tt} ({(a/tt*100):.0f}%)")

        if st.button("New session"):
            st.session_state.iniciado = False
            st.rerun()
        st.stop()

    # ---- Pregunta actual ----
    p = sesion[idx]
    st.markdown(f'<span class="tarea-tag">{p["tarea"]}</span>', unsafe_allow_html=True)
    st.progress((idx) / total)
    st.markdown(f"**Question {idx + 1} of {total}**  ·  Score: {st.session_state.aciertos}")
    st.markdown(f"### {p['pregunta']}")

    if not st.session_state.respondida:
        seleccion = st.radio("Choose one answer:", p["opciones"],
                             index=None, key=f"radio_{idx}")
        if st.button("Submit answer"):
            if seleccion is None:
                st.warning("Please select an answer first.")
            else:
                st.session_state.seleccion = seleccion
                st.session_state.respondida = True
                ok = (seleccion == p["respuesta"])
                if ok:
                    st.session_state.aciertos += 1
                st.session_state.historial.append((idx, ok))
                st.rerun()
    else:
        seleccion = st.session_state.seleccion
        ok = (seleccion == p["respuesta"])
        for op in p["opciones"]:
            if op == p["respuesta"]:
                st.markdown(f'<div class="correcto">&#10003; {op}</div>', unsafe_allow_html=True)
            elif op == seleccion and not ok:
                st.markdown(f'<div class="incorrecto">&#10007; {op} (your answer)</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="padding:8px 12px;color:#9fb3c8;">{op}</div>', unsafe_allow_html=True)

        if ok:
            st.markdown('<div class="correcto"><b>Correct!</b></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="incorrecto"><b>Incorrect.</b></div>', unsafe_allow_html=True)

        st.markdown(f'<div class="explicacion"><b>Explanation:</b> {p["explicacion"]}</div>',
                    unsafe_allow_html=True)

        label = "Next question" if idx + 1 < total else "See results"
        if st.button(label):
            st.session_state.idx += 1
            st.session_state.respondida = False
            st.session_state.seleccion = None
            st.rerun()
