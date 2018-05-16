<%inherit file="layout.mako"/>
<div class="content">
  <h1>Tables</h1>
  <table class="table table-condensed table-hover table-stripped">
  <thead><tr>
    <th>Table
    <th>Primary keys
  <tbody>
  % for i in _context.tables:
    <tr><td><a href="${ request.resource_url(_context, i) }">${ i }</a>
        <td>
        % for pk in _context.tables[i].primary_key:
            ${ pk }
        % endfor
  % endfor
  </table>
</div>

