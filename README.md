<table align="center"><tr><td align="center" width="9999">
<img src="/docs/assets/etalab.jpg" align="center" alt="Project icon">

# Albert

| <a href="https://www.etalab.gouv.fr/"><b>Etalab</b></a> | <a href="https://github.com/etalab-ia/albert/tree/main/docs"><b>Documentation</b></a> | <a href="https://huggingface.co/AgentPublic"><b>HuggingFace</b></a> | 

</td></tr></table>

*[English version below](#english-version)*

## À propos

Albert est un projet d'agents conversationnels (*large language models*, LLM) pour l'administration française, développé par les équipes du Datalab d'[Etalab](https://www.etalab.gouv.fr/) de la [Direction Interministérielle du Numérique (DINUM)](https://www.numerique.gouv.fr/dinum/). Pour toutes questions relatives à Albert, vous pouvez contacter l'équipe à l'adresse [etalab@modernisation.gouv.fr](etalab@modernisation.gouv.fr).

Ce dépôt permet de déployer deux services :
- les modèles *Albert* et leur API

   > 💡 **Les différents modèles sont disponibles dans le dépôt HuggingFace [AgentPublic](https://huggingface.co/AgentPublic).**

- une API permettant d'interroger l'API du modèle à l'aide d'une base de connaissance (*Retrivial Augmented Generated*, RAG)

Vous trouverez également d'autres dépôts liés à Albert :

- [albert-frontend](https://github.com/etalab-ia/albert-frontend) (bientôt disponible) : une interface web pour interagir avec l'API Albert sous forme de chatbot
  
- [albert-tchapbot](https://github.com/etalab-ia/albert-tchapbot) : un chatbot Albert pour l'application Tchap (Messagerie instantanée de l'État)

## Documentation 

Vous trouverez l'ensemble de la documentation en français dans le dossier *[/docs/fr](./docs/fr/)* :
* [Installation](/docs/fr/installation.md)
* [Pour lancer l'API Albert en local (dev mode)](/docs/fr/api-dev.md)
* [Pour obtenir un jeton d'accès à l'API Albert](/docs/fr/api-token.md)
* [Bases de données](/docs/fr/databases.md)
* [Modèles supportés](/docs/fr/modeles.md)
* [Pour configurer les templates de prompt](/docs/en/prompt.md)
* [PyAlbert](/docs/fr/pyalbert.md)

## Wiki

Vous trouverez également des informations complémentaires telles que :
* [Les stratégies de génération](/docs/fr/generation.md)

## Code source

Pour récupérer la dernière version du code :
```bash
git clone https://github.com/etalab-ia/albert.git
```

## Contribuer au projet

Le projet est en open source, sous [licence MIT](LICENCE). Toutes les contributions sont bienvenues, sous forme de pull requests ou d'ouvertures d'issues sur le repo officiel [GitHub](https://github.com/etalab-ia/albert).

Avant de contribuer au dépôt, il est nécessaire d'initialiser les _hooks_ de _pre-commit_ :
```bash
pre-commit install
```

Si vous ne pouvez pas utiliser de pre-commit, il est nécessaire de formatter, linter et trier les imports avec [Ruff](https://docs.astral.sh/ruff/) avant chaque commit :
```bash
ruff check --fix --select I .
```

---

# English version

<details>
  <summary>English version</summary>

## About

Albert is a project of conversational agents (*large language models*, LLM) for the French administration, developed by the Datalab teams of [Etalab](https://www.etalab.gouv.fr/) from the [Direction Interministérielle du Numérique (DINUM)](https://www.numerique.gouv.fr/dinum/). For any questions regarding Albert, you can contact the team at [etalab@modernisation.gouv.fr](etalab@modernisation.gouv.fr).

This repository allows the deployment of two services:

- The Albert models and their API

   > 💡 **The models are available in the HuggingFace repository [AgentPublic](https://huggingface.co/AgentPublic).**

- An API allowing to query the model's API using a knowledge base ([Retrieval Augmented Generation, RAG](https://en.wikipedia.org/wiki/Prompt_engineering#Retrieval-augmented_generation))

You will also find other repositories related to Albert:

- [albert-frontend](https://github.com/etalab-ia/albert-frontend) (soon available): a web interface to interact with the Albert API as a chatbot

- [albert-tchapbot](https://github.com/etalab-ia/albert-tchapbot): a chatbot Albert for the Tchap application (Instant messaging app of the French State)

## Documentation 

You will find all the documentation in Engligh in the folder *[/docs/en](./docs/en/)*:
* [Installation](/docs/en/installation.md)
* [To run the Albert API locally (dev mode)](/docs/en/api-dev.md)
* [To get an access token for the Albert API](/docs/en/api-token.md)
* [Databases](/docs/en/databases.md)
* [Supported models](/docs/en/modeles.md)
* [To configure prompts templates](/docs/en/prompt.md)
* [PyAlbert](/docs/en/pyalbert.md)

## Wiki

You will also find additional information such as:
* [Generation strategies](/docs/en/generation.md)

## Clone source code

To get the latest version of the code:
```bash
git clone https://github.com/etalab-ia/albert.git
```

## Contributing

The project is open source, under the [MIT license](LICENCE). All contributions are welcome, in the form of pull requests or issue openings on [GitHub](https://github.com/etalab-ia/albert).

Before contributing to the repository, it is necessary to initialize the pre-commit hooks:
```bash
pre-commit install
```

If you cannot use pre-commit, it is necessary to format, lint, and sort imports with [Ruff](https://docs.astral.sh/ruff/) before committing:
```bash
ruff check --fix --select I .
```

</details>
