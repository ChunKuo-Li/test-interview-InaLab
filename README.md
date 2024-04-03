# Note: 
All the 7 original requirements are labeled and listed in the 2nd half of this page at the 'Reference' section

# Usage of the 'test-interview-InaLab' repository:
1. On an AWS EC2 ubuntu instance terminal, do:
   "cd ~"
2. Get the code package from GitHub repository of ChunKuo Li by:
   "git clone https://github.com/ChunKuo-Li/test-interview-InaLab.git"
            --->>> this satisfies [[Req_7: Push your solution to your own repository on GitHub, GitLab, another public repository, or provide an archive file (.zip) to the 
   team.]]
3. Change into the working directory:
   "cd test-interview-InaLab"
4. In this working directory, there are 7 files with 4 major ones mentioned here, and 1 sub-directory '/files':
   * "Dockerfile" --->>> this satisfies [[Req_1: Provide a `Dockerfile` to build and run the application.]]
   * "docker-compose.yml" --->>> this satisfies [[Req_3: Provide a `docker-compose.yml` file to run the application and set a custom
   string using an environment variable.]] & it contains a section for Nginx service in this file, thus it also satisfies [[Req_6: Idea: Try the [nginx](https://hub.docker.com/_/nginx) or [traefik](https://hub.docker.com/_/traefik) Docker 
   image ran from the same Docker Compose file as the application.]]
   * "parse_json.py" --->>> this satisfies [[Req_4: Provide a script or code in a language or tool of your choice that will parse
    the data returned from <http://localhost:5000/data> and create a file in a `files/` sub-directory named `<id>.txt` with the _name_ as the contents of the
    file.]]
   * "nginx.conf" --->>> this satisfies [[Req_6: Idea: Try the [nginx](https://hub.docker.com/_/nginx) or [traefik](https://hub.docker.com/_/traefik) Docker 
   image ran from the same Docker Compose file as the application.]]
5. Run Docker compose, do:
   "sudo docker compose build && sudo docker compose up"
6. Open the 2nd terminal that connects to the same EC2 instance, do:
   "curl http://localhost:5000"
7. On the same 2nd terminal, it will return:
   "Hello, World!" --->>> this satisfies [[Req_2: Modify the application to replace _Hello, World!_ with an optional string set
    using an environment variable and defaulting to _Hello, World!]] & [[Req_6: Idea: Try the nginx or traefik Docker image ran from the same Docker Compose file as the application.]]
8. Still on the 2nd terminal, do:
   "curl http://localhost:5000/data > ~/test-interview-InaLab/data.json"
9. Back onto the 1st terminal, do:
    "Ctrl+C" & "Ctrl+C" again to exit from the 'docker compose' command.
10. On the 1st terminal, do:
   "python3 parse_json.py" --->>> this takes the output of step #8 'data.json' as input file to this step and parse it to generate the required output files, this satisfies [[Req_4: Provide a script or code in a language or tool of your choice that will parse the data returned from <http://localhost:5000/data> and create a file in a `files/` sub-directory named `<id>.txt` with the _name_ as the contents of the
    file.]]
11. On the 1st terminal, it will return on screen: 
   "File 7692c3ad3540bb803c020b3aee66cd8887123234ea0c6e7143c0add73ff431ed.txt created and SHA256 sum matches id!
    File 3fc4ccfe745870e2c0d99f71f30ff0656c8dedd41cc1d7d3d376b0dbe685e2f3.txt created and SHA256 sum matches id!
    File 8b5b9db0c13db24256c829aa364aa90c6d2eba318b9232a4ab9313b954d3555f.txt created and SHA256 sum matches id!"
    --->>> this satisfies [[Req_5: Note: The SHA256 sum of each file's contents (`<name>`) should match the `<id>`]]
12. Still on the 1st terminal, change directory by:
    "cd /files" and do: "ls -al"
13. It returns 3 files with the freshing timestamp about just few seconds ago: 
    "3fc4ccfe745870e2c0d99f71f30ff0656c8dedd41cc1d7d3d376b0dbe685e2f3.txt,
     7692c3ad3540bb803c020b3aee66cd8887123234ea0c6e7143c0add73ff431ed.txt,
     8b5b9db0c13db24256c829aa364aa90c6d2eba318b9232a4ab9313b954d3555f.txt"
14. View the content of each file by:
    "more 3fc4ccfe745870e2c0d99f71f30ff0656c8dedd41cc1d7d3d376b0dbe685e2f3.txt", it returns: "two";
    "more 7692c3ad3540bb803c020b3aee66cd8887123234ea0c6e7143c0add73ff431ed.txt", it returns: "one";
    "more 8b5b9db0c13db24256c829aa364aa90c6d2eba318b9232a4ab9313b954d3555f.txt", it returns: "three";
    --->>> this satisfies [[Req_4: Provide a script or code in a language or tool of your choice that will parse the data returned from <http://localhost:5000/data> and create a file in a `files/` sub-directory named `<id>.txt` with the _name_ as the contents of the file.]]
15. Once all the steps successfully complete, exit both terminal 1 & 2.

# Reference
## InaLab Interview Assignment Requirements:

## Docker Exercise

* Req_1: Provide a `Dockerfile` to build and run the application.
* Req_2: Modify the application to replace _Hello, World!_ with an optional string set
  using an environment variable and defaulting to _Hello, World!_
* Req_3: Provide a `docker-compose.yml` file to run the application and set a custom
  string using an environment variable.

This should result in the ability to navigate to <http://localhost:5000/> and see
the custom greeting.

## Scripting Exercise

* Req_4: Provide a script or code in a language or tool of your choice that will parse
the data returned from <http://localhost:5000/data> and create a file in a
`files/` sub-directory named `<id>.txt` with the _name_ as the contents of the
file.
E.g. `files/3fc4ccfe745870e2c0d99f71f30ff0656c8dedd41cc1d7d3d376b0dbe685e2f3.txt`

* Req_5: Note: The SHA256 sum of each file's contents (`<name>`) should match the `<id>`.

## Reverse Proxy Configuration

Provide a minimal reverse proxy configuration for the application. This can be anything -
an Nginx, Apache, or Traefik config, a Terraform, CloudFormation, or CDK
configuration for AWS Load Balancing, etc.

It does not have to be implemented and functional in this exercise.

* Req_6: Idea: Try the [nginx](https://hub.docker.com/_/nginx) or
[traefik](https://hub.docker.com/_/traefik) Docker image ran from the same
Docker Compose file as the application.

## Submittal

* Req_7: Push your solution to your own repository on GitHub, GitLab, another public
repository, or provide an archive file (.zip) to the team.
