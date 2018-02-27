# AdeBot

## Comandi per fare l'upload

* Usa `heroku logs -a fancazzistibot --tail` per visualizzare i dettagli del log.
* Usa `./commitAndPush` per fare l'upload dei cambiamenti 

## Other
If the bot is experiencing some unwanted behavior you would want to kill it, use:
`heroku ps:scale web=0` in the terminal window where your repository is located to kill the application
To restart it use `heroku ps:scale web=1`

If you want to connect to the database use the command:
`heroku pg:psql`