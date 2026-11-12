from components.layout import Layout
from components.navbar import navbar
from components.hero import hero
from components.about import about
from components.work_strip import work_strip
from components.contact_section import contact_section

# ----------------------------------------------------------
# PAGE SETUP
# ----------------------------------------------------------

Layout.setup()

# ----------------------------------------------------------
# PAGE CONTENT
# ----------------------------------------------------------

navbar()

hero()

about()

work_strip()

contact_section()