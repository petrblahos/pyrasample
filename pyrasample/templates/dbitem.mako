<%inherit file="layout.mako"/>
<%!
from urllib.parse import urlencode
%>
<div class="content">
  <h1>${ _context.__parent__.model.name }</h1>
  <form class="form-horizontal">
  % for (field, value) in _context.item._asdict().items():
    <div class="form-group">
      <label for="input_${ field }" class="col-sm-2 control-label">${ field }</label>
      <div class="col-sm-10">
        <input class="form-control" id="input_${ field }" value="${ value }">
      </div>
    </div>
  % endfor
  </form>
</div>

