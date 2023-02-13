---
title: "Core"
weight: 10
---

In this section, we will provide information about the core part of PrCore.

## Class diagram

The following diagram shows the structure of the core classes.

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
        outcome_definition: list[list[dict[str, datetime | float | int | str]]]
        treatment_definition: list[list[dict[str, datetime | float | int | str]]]
        fast_mode: bool
        start_transition: str
        end_transition: str
    }

    class Project {
        id: int
        created_at: datetime
        updated_at: datetime
        name: str
        description: str
        status: str
        selected_plugins: list[str]
        event_log: EventLog
        cases: list[Case]
        events: list[Event]
        plugins: list[Plugin]
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

    class Plugin {
        id: int
        key: str
        name: str
        prescription_type: str
        description: str
        parameters: dict[str, str | bool | int | float]
        status: str
        model_name: str
        project: Project
    }

    EventLog "1" -- "1" Definition
    Project "1" -- "1" EventLog
    Project "1" -- "n" Case
    Project "1" -- "n" Event
    Case "1" -- "n" Event
    Project "1" -- "n" Plugin
{{< /mermaid >}}
