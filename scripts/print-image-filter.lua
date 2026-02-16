-- print-image-filter.lua
-- Rewrites static image paths from images/generated/ to images/generated/print/
-- for the print-kdp profile, using PDF versions for vector-quality output.
-- Referenced by _quarto-print-kdp.yml.

function Image(el)
  local src = el.src
  -- Match paths ending in images/generated/<filename> (not already in print/)
  local new_src = src:gsub("(images/generated/)([^/]+)$", "%1print/%2")
  if new_src ~= src then
    -- Prefer PDF version for print output (vector, no rasterization)
    new_src = new_src:gsub("%.png$", ".pdf")
    el.src = new_src
  end
  return el
end
