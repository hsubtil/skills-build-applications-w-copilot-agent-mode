import { useEffect, useMemo, useState } from 'react';

function ApiResourceTable({ title, endpointPath }) {
  const [rows, setRows] = useState([]);
  const [query, setQuery] = useState('');
  const [selectedRow, setSelectedRow] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const endpoint = useMemo(() => {
    const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
    const baseUrl = codespaceName
      ? `https://${codespaceName}-8000.app.github.dev`
      : 'http://localhost:8000';
    return `${baseUrl}${endpointPath}`;
  }, [endpointPath]);

  const columns = useMemo(() => {
    if (!rows.length || typeof rows[0] !== 'object' || rows[0] === null) {
      return ['data'];
    }

    const keys = Object.keys(rows[0]);
    return keys.slice(0, 5);
  }, [rows]);

  const filteredRows = useMemo(() => {
    const trimmed = query.trim().toLowerCase();
    if (!trimmed) {
      return rows;
    }
    return rows.filter((row) => JSON.stringify(row).toLowerCase().includes(trimmed));
  }, [rows, query]);

  async function loadData() {
    setLoading(true);
    setError('');
    try {
      console.log(`${title} endpoint:`, endpoint);
      const response = await fetch(endpoint);
      const data = await response.json();
      console.log(`${title} fetched data:`, data);

      const normalizedData = Array.isArray(data)
        ? data
        : Array.isArray(data.results)
          ? data.results
          : [];

      setRows(normalizedData);
    } catch (fetchError) {
      console.error(`${title} fetch error:`, fetchError);
      setError('Unable to fetch data from the REST API endpoint.');
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [endpoint]);

  return (
    <section className="mb-4">
      <div className="card shadow-sm border-0">
        <div className="card-body">
          <div className="d-flex flex-wrap justify-content-between align-items-center gap-2 mb-3">
            <h2 className="h4 text-primary mb-0">{title}</h2>
            <a className="link-primary fw-semibold" href={endpoint} target="_blank" rel="noreferrer">
              Open API endpoint
            </a>
          </div>

          <form className="row g-2 mb-3" onSubmit={(event) => event.preventDefault()}>
            <div className="col-md-8">
              <label htmlFor={`${title}-search`} className="form-label fw-semibold">
                Search records
              </label>
              <input
                id={`${title}-search`}
                type="text"
                className="form-control"
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                placeholder="Filter rows by any field value"
              />
            </div>
            <div className="col-md-4 d-flex align-items-end">
              <button type="button" className="btn btn-primary w-100" onClick={loadData} disabled={loading}>
                {loading ? 'Refreshing...' : 'Refresh data'}
              </button>
            </div>
          </form>

          {error && <div className="alert alert-danger">{error}</div>}

          <div className="table-responsive">
            <table className="table table-striped table-hover align-middle mb-0">
              <thead className="table-dark">
                <tr>
                  {columns.map((column) => (
                    <th key={column} scope="col">
                      {column}
                    </th>
                  ))}
                  <th scope="col" className="text-end">
                    Actions
                  </th>
                </tr>
              </thead>
              <tbody>
                {!filteredRows.length && (
                  <tr>
                    <td colSpan={columns.length + 1} className="text-center py-4 text-muted">
                      No data available.
                    </td>
                  </tr>
                )}
                {filteredRows.map((row, index) => (
                  <tr key={row.id || row._id || index}>
                    {columns.map((column) => (
                      <td key={`${row.id || index}-${column}`}>
                        {typeof row === 'object' && row !== null
                          ? String(row[column] ?? '-')
                          : JSON.stringify(row)}
                      </td>
                    ))}
                    <td className="text-end">
                      <button
                        type="button"
                        className="btn btn-outline-secondary btn-sm"
                        onClick={() => setSelectedRow(row)}
                      >
                        View details
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {selectedRow && (
        <>
          <div className="modal fade show d-block" tabIndex="-1" role="dialog" aria-modal="true">
            <div className="modal-dialog modal-lg modal-dialog-scrollable" role="document">
              <div className="modal-content">
                <div className="modal-header">
                  <h3 className="modal-title h5">{title} record details</h3>
                  <button
                    type="button"
                    className="btn-close"
                    aria-label="Close"
                    onClick={() => setSelectedRow(null)}
                  />
                </div>
                <div className="modal-body">
                  <pre className="mb-0">{JSON.stringify(selectedRow, null, 2)}</pre>
                </div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-secondary" onClick={() => setSelectedRow(null)}>
                    Close
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div className="modal-backdrop fade show" />
        </>
      )}
    </section>
  );
}

export default ApiResourceTable;