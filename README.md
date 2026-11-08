# GxLx 1.1.2 — kompilacja Geode na GitHub Actions

To repozytorium służy do zbudowania moda `gxlx.menu.geode` z paczki źródłowej GxLx.

## Jedyny potrzebny upload

1. Wgraj **jeden plik** `GxLx-1.1.2-GitHub-Actions.zip` do głównego katalogu repozytorium: **Add file → Upload files → Commit changes**. Nie wypakowuj archiwum.
2. GitHub Actions automatycznie uruchomi workflow **Build GxLx 1.1.2 from ZIP**.
3. Po udanej kompilacji otwórz Actions → ostatnie wykonanie → Artifacts i pobierz `GxLx-1.1.2-Windows`.
4. Rozpakuj `gxlx.menu.geode` i przenieś do folderu `Geometry Dash/geode/mods`.

Konfiguracja jest przeznaczona dla **Windows x64**, **Geometry Dash 2.2081**, **Geode SDK 5.11.2**. Workflow nie jest potwierdzony kompilacją, dlatego w razie błędu należy sprawdzić logi w Actions.

Kod GxLx bazuje na Eclipse Menu (EPL-2.0); zachowaj oryginalne informacje licencyjne z paczki.
