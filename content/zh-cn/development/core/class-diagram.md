---
title: "类图"
weight: 20
---

The system is structured using several core classes, as depicted in the diagram. The EventLog class represents the event log file and contains details such as the file name, saved name, and associated Definition object. The Definition class contains definitions necessary for system training, such as column definitions, case attributes, outcome definitions, and treatment definitions, among others.

The Project class represents a project that uses the PrCore system for prescriptive process monitoring. It contains details such as the project name, description, and associated EventLog object, as well as a list of associated Plugin objects.

The Plugin class represents a plugin in the system and contains details such as the plugin name, description, and status.

The Event and Case classes used to represent events and cases in the stream data. By utilizing these classes for storing stream data, the PrCore system can provide timely and prescribing recommendations for ongoing cases, allowing users to make informed decisions about their processes.

Overall, the system design is highly structured and organized, with each class containing details essential for efficient prescriptive process monitoring.

{{< mermaid class="text-center" >}}
classDiagram
    class EventLog {
        id: int
        created_at: datetime
        updated_at: datetime
        file_name: str
        saved_name: str
        df_name: str
        training_df_name: str
        simulation_df_name: str
        definition: Definition
    }

    class Definition {
        id: int
        created_at: datetime
        updated_at: datetime
        columns_definition: dict[str, str]
        case_attributes: list[str]
        fast_mode: bool
        start_transition: str
        complete_transition: str
        abort_transition: str
        outcome_definition: list[list[dict[str, str]]]
        treatment_definition: list[list[dict[str, str]]]
    }

    class Project {
        id: int
        created_at: datetime
        updated_at: datetime
        name: str
        description: str
        status: str
        error: str
        selected_plugins: list[str]
        event_log: EventLog
        plugins: list[Plugin]
    }

    class Plugin {
        id: int
        created_at: datetime
        updated_at: datetime
        project_id: int
        key: str
        prescription_type: str
        name: str
        description: str
        parameters: dict[str, str | bool | int | float]
        additional_info: dict[str, Any]
        status: str
        error: str
        disabled: bool
        model_name: str
        project: Project
    }

    class Case{
        id: int
        created_at: datetime
        updated_at: datetime
        project_id: int
        case_id: str
        completed: bool
        events: list[Event]
    }

    class Event{
        id: int
        created_at: datetime
        updated_at: datetime
        project_id: int
        attributes: dict[str, str | bool | int | float | None]
        prescriptions: dict[str, Any]
        prescribed: bool
        sent: bool
        case: Case
    }

    EventLog "1" -- "1" Definition
    Project "1" -- "1" EventLog
    Project "1" -- "*" Plugin
    Project "1" -- "*" Case
    Project "1" -- "*" Event
    Case "1" -- "*" Event
{{< /mermaid >}}
