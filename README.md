
# AlamoBot
Un irreverente bot open-source para Discord

## Comenzar

Estas instrucciones proveen lo necesario para hacer subir a AlamoBot a Heroku

### Prerequisitos entorno local

Se requieren las siguientes dependencias en caso de usar el bot localmente:

```
discord.py
aiohttp
asyncio
logbook
ujson

Versión de Python: 3.6.5
```

Al elegir hacerlo localmente asumo que sabes lo que haces por lo cual no brindaré más información al respecto.

### Prerequisitos Heroku

Proveemos todos los archivos necesarios para el deployment en Heroku, solamente necesitas crear una aplicación y bot de discord [aquí](https://discordapp.com/developers).

Sin embargo para realizar el deployment es necesario cuentes con algunas aplicaciones (*ajenas este proyecto*):

* [Git](https://git-scm.com/downloads) - Para control de versiones y push a repositorio de Heroku
* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) - Para iniciar sesión y crear app en Heroku
* [Pipenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) - Instalable mediante `pip` con Python: `pip install pipenv`

## APIs utilizadas

* [OpenWeatherMap](https://openweathermap.org) - Utilizada en comando `&clima`


## Deployment a Heroku

Se proveen los pasos que seguí personalmente para hacer el deployment a Heroku, recomiendo seguir paso a paso.

### Editar cfg.json.example

Se debe modificar el archivo y guardarse eliminando el `.example` al final, debe tener el nombre `cfg.json`

```javascript
{
	"discord":{
		"prefijo": "&",
		"token": ""
	},
	"api":{
		"provider": "YH",
		"key": {
			"OWM": ""
		}
	}
}
```

#### Consideraciones

* En `prefijo` se encuentra asignado por default `&` sin embargo puede modificarse al simbolo que se desee.
* `token` requiere del token del bot que se haya generado en Discord
* En `provider` utilizar una de dos opciones disponibles, `YH` para Yahoo! Weather y `OWM` para OpenWeatherMap, utilizar `OWM` es necesario proveer una API Key dentro de `key`.

### Iniciar sesión en Heroku

Mediante la terminal ingresar `heroku login` y proveer los datos solicitados:

```bash
heroku login
```

Ejemplo de prompt despues del comando:
```bash
Enter your Heroku credentials.
Email: correo@ejemplo.com
Password:
...
```

Posteriormente deben clonar este repositorio e ingresar a la carpeta resultante:

```bash
git clone https://github.com/garaekz/alamobot.git
cd alamobot
```

Una vez en la carpeta del proyecto deberán crear una nueva aplicación de Heroku:
```bash
heroku create
```

Ejemplo de prompt despues del comando:
```bash
Creating lit-bastion-5032 in organization heroku... done, stack is cedar-14
http://lit-bastion-5032.herokuapp.com/ | https://git.heroku.com/lit-bastion-5032.git
Git remote heroku added
...
```

Por último:
```bash
git push heroku master
```

Aparecerá algo como lo siguiente y habrás terminado:
```bash
Counting objects: 232, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (217/217), done.
Writing objects: 100% (232/232), 29.64 KiB | 0 bytes/s, done.
Total 232 (delta 118), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote: -----> Installing python-3.6.5
remote: -----> Installing requirements with latest pipenv...
remote:        Installing dependencies from Pipfile.lock...
remote:      $ python manage.py collectstatic --noinput
remote:        58 static files copied to '/app/gettingstarted/staticfiles', 58 post-processed.
remote:
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 39.3M
remote: -----> Launching...
remote:        Released v4
remote:        http://lit-bastion-5032.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To git@heroku.com:lit-bastion-5032.git
 * [new branch]      master -> master
```

#### Consideraciones

* Asegurate que en Heroku esté activado el worker
* Invita a tu bot al servidor deseado

## Autor

* **David Garay** - *Contribuyente único* - [Garaekz](https://github.com/garaekz/)

## Aclaraciones

* La estructura de los archivos y el uso de `logbook` fue inspirada por el repositorio del bot [Pixie](https://github.com/GetRektByMe/Pixie)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.