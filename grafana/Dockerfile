FROM grafana/grafana-oss:latest

# Install the SQLite plugin (DuckDB works because of SQLite compatibility)
RUN grafana-cli plugins install frser-sqlite-datasource