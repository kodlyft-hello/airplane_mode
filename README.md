### Airplane Mode

An airplan app for an airline

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app airplane_mode
```

### Airport Shop Management

- **Shops:** create an Airport Shop for each shop at an airport. Entering a tenant marks the shop Occupied, and clearing the tenant makes it Available again. Each Airport shows its total, available and occupied shop counts.
- **Settings:** in Airport Shop Settings, set the default monthly rent for new shops and turn the monthly rent reminder emails on or off. Reminders need an outgoing Email Account.
- **Rent:** open an occupied shop and click Collect Rent to record one Shop Rent Payment per month. Print it with the Rent Receipt format.
- **Shop Types:** Stall, Walk-through and Normal are installed with the app. Untick Enabled? on a type to hide it from the shop form.
- **Flights:** add the crew under Crew Members. Changing a flight's Gate Number updates the gate on all its tickets in the background.
- **Website:** `/shops` lists every shop, each shop has its own page, and `/shop-lead/new` collects enquiries from people interested in renting.

#### REST API (Bruno)

Open the `bruno` folder in [Bruno](https://www.usebruno.com/) and select the `airline` environment. Then fill in `api_key` and `api_secret` from User > Settings > API Access > Generate Keys. Every request sends `Authorization: token <api_key>:<api_secret>`.

- **List Shops:** `GET /api/resource/Airport Shop?fields=["*"]&limit_page_length=0`
- **Create Shop:** `POST /api/resource/Airport Shop` with a JSON body

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/airplane_mode
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade
### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
