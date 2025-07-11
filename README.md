# binaryflux-content-ootb-repository


# lookups

Use these lookup data to enrich events. Import it into minio or s3 by create a bucket called lookups and import them via the lookup functionlity in the binaryflux application.

## Maxmindipv4
    Description: Provides geolocation information for IPv4 addresses using Maxmind’s processed GeoLite2-Country-Blocks data
    Path: s3://lookups/maxmind/GeoLite2-Country-Blocks-IPv4-processed.csv
## Maxmindipv6
    Description: Provides geolocation information for IPv6 addresses using Maxmind’s processed GeoLite2-Country-Blocks data
    Path: s3://lookups/maxmind/GeoLite2-Country-Blocks-IPv6-processed.csv
## Maxmindcountries
    Description: Provides geolocation countries data using Maxmind’s processed GeoLite2-Country-Locations data
    Path: s3://lookups/maxmind/GeoLite2-Country-Locations-en.csv
## MitreTactics
    Description: Provides comprehensive data on MITRE tactics and their descriptions, aiding in threat intelligence and cybersecurity analysis
    Path: s3://lookups/mitre/mitre_tactics_and_description.csv
## MitreTechniques
    Description: Provides detailed information on MITRE techniques along with their descriptions, facilitating advanced threat intelligence analysis
    Path: s3://lookups/mitre/mitre_tactics_and_techniques.csv
## BinaryfluxFields
    Description: Reserved binaryflux data fields
    Path: s3://lookups/binaryflux/binaryflux_fields_minimal.csv

Usage:
  > Use the ipaddress to get its quivalent int value\
  ```ip_int = range.toIpLong(ip)```

  > If its an ipv6 then call below to get the country data\
  ```country_data = tpi.query("Maxmindipv6", "? BETWEEN start_ip AND end_ip", [ip_int])```

  > If its an ipv4 then call below to get the country data\
  ```country_data = tpi.query("Maxmindipv4", "? BETWEEN start_ip AND end_ip", [ip_int])```

  > You can access the geolocation id using below\
  ```geo_id = country_data[0][2]```

  > To get the country details use below\
  ```country = tpi.query("Maxmindcountries", "geoname_id=?", [geo_id])```
  ```country_name = country[0][5]```
