// Module  : apps.desktop.src-tauri.main
// Purpose : Tauri Rust shell entry point. Registers IPC command handlers
//           for native OS operations: file system dialogs, sandboxed process
//           spawning, and system tray management. Bridges Rust backend
//           with the React frontend via Tauri's IPC channel.
// Layer   : Desktop — Native Shell (Tauri)

#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

fn main() {
    tauri::Builder::default()
        .run(tauri::generate_context!())
        .expect("error while running Cockroach desktop");
}
