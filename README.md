[![Container](https://github.com/morenod/estefanIA/actions/workflows/container-publish.yml/badge.svg)](https://github.com/morenod/estefanIA/actions/workflows/container-publish.yml) [![Code Tests](https://github.com/morenod/estefanIA/actions/workflows/code-tests.yml/badge.svg)](https://github.com/morenod/estefanIA/actions/workflows/code-tests.yml)

# EstefanIA
Bot for interacting with [OpenAI](https://openai.com/) using a chat or Dall-E

## Arguments
| Argument | Description | Environment Variable |
| --- | --- | --- |
| --bot-token | Telegram bot token. Talk to @botfather to get it. | `ESTEFANIA_BOT_TELEGRAM_TOKEN` |
| --allowed-users | List of Telegram user ids (not usernames) authorized to talk to the bot. | `ESTEFANIA_BOT_TELEGRAM_USERNAMES` |
| --log-level | Logging level for log output. Default value is 'INFO'. | `ESTEFANIA_BOT_LOG_LEVEL` |
| --log-file | Path to the log file. | `ESTEFANIA_BOT_LOG_FILE` |
| --openai-org | OpenAI organization ID. | `ESTEFANIA_BOT_OPENAI_ORG` |
| --openai-token | Authentication token for OpenAI. | `ESTEFANIA_BOT_OPENAI_TOKEN` |
| --openai-model | OpenAI model ID to use. | `ESTEFANIA_BOT_OPENAI_MODEL` |

All arguments can be passes to the bot both using the parameter or the envvar, for example:

```
python bot.py --openai-model gpt-4
```
```
ESTEFANIA_BOT_OPENAI_MODEL=gpt4 python bot.py
```

## Available commands
| Command | Description |
| --- | --- |
/estefania | Interact with OpenAI using Chat |  
/photofania  | Generate a Dall-E picture based on the text provided

## Run as container
To run estefanIA as container, save a file with all the parameter and use it as `--env-file`
```
podman run -d -it --name estefanIA --env-file /tmp/env_file ghcr.io/morenod/estefania:latest
```
