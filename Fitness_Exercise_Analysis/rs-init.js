// Inizializzazione del replica set rs0 (da eseguire una sola volta):
//   docker compose exec mongo1 mongosh --port 27017 --quiet /rs-init.js
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "localhost:27017" },
    { _id: 1, host: "localhost:27018" },
    { _id: 2, host: "localhost:27019" },
  ],
});
