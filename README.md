<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/dyte-submissions/november-2023-hiring-Raghavendiran-2002">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">LoggerX</h3>

</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)
LoggerX is a log management solution designed to seamlessly ingest, organize, and swiftly retrieve vast volumes of log data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![React][React.js]][React-url]
- [![NodeJS][Node-url]][Node.js]
- [![Python][Python-url]][Python]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Install Docker and Docker-compose

  ```
  curl -fsSL https://get.docker.com -o get-docker.sh
  ```

  ```
  sudo sh get-docker.sh
  ```

  ```
  sudo apt install docker-compose -y
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/dyte-submissions/november-2023-hiring-Raghavendiran-2002
   ```
2. Navigate to Project Directory
   ```
   cd november-2023-hiring-Raghavendiran-2002/
   ```
3. Start the Application
   ```
   sudo docker-compose up -d
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

View Console :

```
http://localhost:3001
```

View CLI :

```
http://localhost:3000
```

### Using CURL

Fetch all Logs

```curl
curl -X GET http://localhost:3000/fetch-all-logs
```

Fetch Logs

```curl
curl -X GET http://localhost:3000/query-interface?filter=timestamp&start=2023-09-15T08:00:00Z&end=2023-11-15T08:00:00Z
```

```
curl -X GET http://localhost:3000/query-interface?search=12&filter=resourceId
```

Post Logs

```
curl -X POST http://localhost:3000/log-ingestor
   -H 'Content-Type: application/json'
   -d '{
	"level": "error",
	"message": "Failed to connect to DB",
    "resourceId": "server-1234",
	"timestamp": "2023-09-15T08:00:00Z",
	"traceId": "abc-xyz-123",
    "spanId": "span-456",
    "commit": "5e5342f",
    "metadata": {
        "parentResourceId": "server-0987"
    }
}'
```

## API Documentation

### Fetch Logs

```http
GET /query-interface?search=r&filter=level
```

| Parameter | Type     | Description                                                                                       |
| :-------- | :------- | :------------------------------------------------------------------------------------------------ |
| `search`  | `string` | **Required**. string to be search                                                                 |
| `filter`  | `string` | **Required**. ["level","message", "resourceId", "traceId", "spanId", "commit","parentResourceId"] |

Responses

```javascript
{
  "logs": [],
  "status": 200
}
```

```http
GET /query-interface?filter=timestamp&start=2023-09-15T08:00:00Z&end=2023-11-15T08:00:00Z
```

| Parameter | Type     | Description                                   |
| :-------- | :------- | :-------------------------------------------- |
| `start`   | `string` | **Required**. DateTime "2023-09-15T08:00:00Z" |
| `end`     | `string` | **Required**. DateTime "2023-09-15T08:00:00Z" |
| `filter`  | `string` | **Required**. ["timestamp"]                   |

Responses

```javascript
{
  "logs": [],
  "status": 200
}
```

### Fetch All Logs

```http
GET /fetch-all-logs
```

Responses

```javascript
{
  "logs": [],
  "status": 200
}
```

### Post Logs

```http
POST /log-ingestor

```

| Parameter | Type   | Description   |
| :-------- | :----- | :------------ |
| `body`    | `JSON` | **Required**. |

#### Body :

```json
{
  "level": "error",
  "message": "Failed to connect to DB",
  "resourceId": "server-1234",
  "timestamp": "2023-09-15T08:00:00Z",
  "traceId": "abc-xyz-123",
  "spanId": "span-456",
  "commit": "5e5342f",
  "metadata": {
    "parentResourceId": "server-0987"
  }
}
```

### Responses

```javascript
{
  "message": "Inserted Successfully",
  "status": 200
}
```

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Raghavendiran N - raghavendiran46461@gmail.com

Project Link: [https://github.com/dyte-submissions/november-2023-hiring-Raghavendiran-2002](https://github.com/dyte-submissions/november-2023-hiring-Raghavendiran-2002)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[Python-url]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python]: https://www.python.org/
[Node-url]: https://img.shields.io/npm/v/npm.svg?logo=nodedotjs
[Node.js]: https://nodejs.org/en/
