# Uptimerobot add URL monitor
Add monitor to uptimerobot trougth github action

If you don't have an account for uptimerobot please take a look on them site [Oficial site uptimerobot](http://uptimerobot.com)

## Usage

```yaml
jobs:
  Add Uptimerobot monitor:
    runs-on: ubuntu-latest
    steps:
      - name: Create URL monitor
        uses: yojota/uptimerobot-addmonitor@v1
        with:
          url_monitor: "https//yojota.cloud"
          API_uptimerobot: ${{ secrets.API_uptimerobot }}

```