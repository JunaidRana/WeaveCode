Docker build commands

docker build -t load_xml_to_neo4j .
docker run --rm load_xml_to_neo4j


DB Creds
Username:neo4j
Password:Inbox@123


To enable DB Service

sudo systemctl enable neo4j.service


To Start DB Service

sudo systemctl start neo4j.service


To see status DB Service

sudo systemctl status neo4j.service



To enable DB Service schell

cypher-shell



MY DB Connected URL
http://localhost:7474/browser/


exit