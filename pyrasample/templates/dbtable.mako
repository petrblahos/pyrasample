<%inherit file="layout.mako"/>
<%!
from urllib.parse import urlencode

ROW_LIMIT = 1000
%>
<div class="content">
  <h1>${ _context.model } <a href="${ request.resource_url(_context, query={"xlsx":1}) }">...xlsx</a></h1>
  <nav aria-label="pager">
    <ul class="pager">
      <li class="previous"><a href="${ request.resource_url(_context, "prev") }"><span aria-hidden="true">&larr;</span> Previous page</a></li>
      <li class="next"><a href="${ request.resource_url(_context, "next") }">Next page <span aria-hidden="true">&rarr;</span></a></li>
    </ul>
  </nav>  
  <table class="table table-hover table-condensed table-striped table-responsive">
  <thead><tr><td>
  % for col in _context.model.columns:
    <th>${ col }
  % endfor
  % for row in request.db.execute(_context.get_query()):
  <%
    link = {}
    for pk in _context.model.primary_key:
        link[pk.name] = row[pk]
    if link:
        link = urlencode(link)
  %>
  <tbody>
    <tr>
        <td class="info"><small>${ loop.index + 1 + _context.page * _context.ITEMS_PER_PAGE }</small>
    % for col in _context.model.columns:
      % if link:
      <td><a href="${ request.resource_url(_context, link) }">${ row[col.name] }</a>
      % else:
      <td>${ row[col.name] }
      % endif
    % endfor
  % endfor
  </table>
  <nav aria-label="pager">
    <ul class="pager">
      <li class="previous"><a href="${ request.resource_url(_context, "prev") }"><span aria-hidden="true">&larr;</span> Previous page</a></li>
      <li class="next"><a href="${ request.resource_url(_context, "next") }">Next page <span aria-hidden="true">&rarr;</span></a></li>
    </ul>
  </nav>  
</div>
