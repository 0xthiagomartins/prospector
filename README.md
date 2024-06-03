# Job opportunity prospector

This project was built with the goal of help me find job opportunities in a easier way;

---

## Usage:

```python
from src.service import Prospector

prospector = Prospector(verbose=True)

domain = "business_domain.com"
business_emails =  prospector.list_emails_from_domain(domain)
```