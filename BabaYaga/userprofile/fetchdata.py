import time
import jwt
import requests 
from jwt.algorithms import RSAAlgorithm
import json
import base64
import chardet

def fetchdata(google_bearer_token):
  SERVICE_ACCOUNT_EMAIL = "babayaga@coriolis-library.iam.gserviceaccount.com"
  PRIVATE_KEY_ID_FROM_JSON = "bf474b8027c98b2ffcccf22855c304bd56290ca7"
  PRIVATE_KEY_FROM_JSON = "-----BEGIN PRIVATE KEY-----\n" \
                          "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCuIEdt00Ydts7e\n" \
                          "WGcrqyslGXooj+a16Br/AZdrE5JgHdjV3T7Qp0JBGdf03Z2R3I+oBfKHMQwCm47J\n" \
                          "Uw/nZ3d2U546vFgb734zVGlEK25OeiEpq7eYIXcrOSVt54AYVwzZM1N+fBpeQxEV\n" \
                          "1vcMleKSPiT/4o4mnWhanmL9+LsYw0mAHtoH9gmmD2yEMuSScffoc4v5GDZhZ9O8\n" \
                          "VJ7zCI03HuHz42KwgeaGCDznGhh2IfhgalqRN9A5z3EPYBAliaZWMDV263oVC0zC\n" \
                          "1ZjmXJcudFayBYh1NCWG2THHJlopKpne0qnE1S6zNJ31FqR1NRK2sVc6XMvzB+YW\n" \
                          "GHEGidZ5AgMBAAECggEAHvseSmOfY5UNnJD1Fld3rzunuQTVg0MfXoTdeI88aX6W\n" \
                          "AINDdGN2Ddg3zNkLepLYOoiIXNZ0sRgVYSu2tjD6F+ML0Z6GPL4xYZegvSDPGQZw\n" \
                          "1RW47kfyCI474yCf8XS3lAOmVOhm1qOvLAgZ37LhY6zL731TVnqGQS1SJqb1PxPg\n" \
                          "wNcUUUIQvYBAgBaC464nCX6s93+4r25yAFQIFMtAEirgSbZDoyOVkB3LN4p7L052\n" \
                          "kSCLp6wD/rSVIdeDQXFI4anAnzxIS/LBMSGV6L8aCS42nZvDLJXOb1oe8JEQZB1T\n" \
                          "kGdL8ZAfYYq7T9zPqm9kRq90iaoHXMVcLINc0I0egwKBgQDgR15/BLOxabReP2H/\n" \
                          "g8QWPvncyLJ/Am+cefrxY8HhTQsXJLvXRYlKJuhu5GQptJo00Y+ZQLEjv6vuu1lk\n" \
                          "rA6WIPTaNt254kPZJd8l8KxeWJhTCYfjr1NohYSzrn7yoxDaRC/ot2V4rWtJRpI8\n" \
                          "DN08htkT0N3CRGyqoWM/2ZM50wKBgQDGwP5UWmYkNpTzGorcSxYEiI+YgZpN3Y5f\n97zCrDc6w0vBT9yB74b99zpXIXyJ6a6JyzoQcdPGLlE4yx1myn3mOJ7yVIGi/m11\n" \
                          "Cu0u8s/lZvkTU5tGpYR2mACWUaXKqo/qF4QLDZaucdgFgwigwmCJdyA21F59YCAR\npXqT1HSTAwKBgQCoLPwv9N+l3mSw84hRqIXGRKzqINiwIqx8wn8ouSwt/K6fSR1N\nvEfJgclzNfHh0Bp+FtI+EeOCsfyEBJpwwhAiBU51vwSemYtU7nAZLBKkoHyAb7ol\nQlgiHVS3w9ZPrXU6pjzinXsKdcfoZ3HKc78F3vwyPsG7JcHyZRheTZF3nwKBgCdM\n/D1zzqS0gkl74x9iXY0x76sJXZiuCbwiQZoA8b7V5UHpZ8HtujS30Tpvba/bnF60\n59telrCmcfsX9s1flvuSEKP8X9H6G2y8Z2AUNVW4QeI3cwnKKuJEdkFDDdSAW4q/\ncaW53yTJcBzO50LajLpB6wXMgo6qFk1G+nEG3rI/AoGBAJlTahyssFQG6WGS8vtJ\nTqIoPm8k/EFn0STyOPdyxn3KxWyiboab8wsTmFxhdvGvyS9aHqFNmWlPrq8MxYwC\nahwualeQh4lR3pDIM/WkhsgVkVWHtByjbAkfa6Piiyqqc4CAbfe361W4ZMpOwRFl\nIbt0V/Pyl3XNP9kj5fFZMzNe" \
                          "\n-----END PRIVATE KEY-----\n"

  PUBLIC_KEY_URL="https://www.googleapis.com/service_accounts/v1/jwk/appscriptcoriolis@employee-2019.iam.gserviceaccount.com"

  header = {
    "alg": "RS256",
    "typ": "JWT",
    "kid": PRIVATE_KEY_ID_FROM_JSON # service account's private key ID.
  }
  iat = time.time()
  exp = iat + 3600
  payload = {
      # For iss and sub specify email address of the service account.
      "iss": SERVICE_ACCOUNT_EMAIL,
      "sub": SERVICE_ACCOUNT_EMAIL,
      "scope": "https://www.googleapis.com/auth/userinfo.email",
      "iat": iat,
      "exp": exp,
      "kid": PRIVATE_KEY_ID_FROM_JSON,
  }
  additional_headers = {'kid': PRIVATE_KEY_ID_FROM_JSON}
  signed_jwt = jwt.encode(payload, PRIVATE_KEY_FROM_JSON,headers=additional_headers, algorithm="RS256")
  # print(signed_jwt)
  url='https://script.google.com/macros/s/AKfycbzQfRFfq7nm_RJaiG_UhvgdWcrvj2befr6tw7UxkrlrYs9kLhY2/exec'
  uri='/auth/token'
  user_token=google_bearer_token
  params={
      'uri':uri,
      'user_token':user_token,
      'app_token':signed_jwt
  }
  access_token_request=requests.post(url,params=params)
  access_token=access_token_request.json()
  IDjwt=access_token["token"]
  header=IDjwt.split('.')[0]
  # print("header is ",header)
  my_kid=base64.b64decode(header)
  my_kid=json.loads(my_kid.decode(chardet.detect(my_kid)["encoding"]))
  # print("my kid is",my_kid["kid"])
  public_key_content=requests.get(PUBLIC_KEY_URL)
  public_key_content=json.loads(public_key_content.content.decode(chardet.detect(public_key_content.content)["encoding"]))

  for public_content in public_key_content["keys"]:
    if(public_content["kid"]==my_kid["kid"]):
      # print("matched")
      my_kid=public_content

  # print("IDJWT is",IDjwt)
  # key_json = '''{
  #       "kid": "fe845b1493c11a84c0628fbc92f1f7cfc119ba90",
  #       "e": "AQAB",
  #       "kty": "RSA",
  #       "alg": "RS256",
  #       "n": "sUclSkWpMN1WQ3MX2MgLlgbB1ADsbD73vpxxBUyB_lpvF2ThG6orBF5_VRxBfpAAFmuFOr0JMn2FPIrUKYBkueRtadPSwUFMz9E5TofrT4YMjUnziGx9RIBXPwpfCmxj7rq_QZihjTNVHvsf6ugdNt8uUjvtZtwoaWvB8WyszT2m3XtMS7pYPzOtv7uVs8Ib67pdrMlBgAwdaKAPJfCvxU4RtTWgBb1282I6188z_sTamn6nSOQjT-yJ8kUSoBCyS2AU51hbOyhI-3Kq4GmIXW5FWn3SICeR2dQPOn4H2fdL14BW3A_Hdtd3xD6aNC6Tk0LN05t8594T8ynfuuyFMw",
  #       "use": "sig"
  #     }'''
  key_json=json.dumps(my_kid)
  public_key = RSAAlgorithm.from_jwk(key_json)
  # print ("public key is ",public_key)
  # print("total",IDjwt,public_key)
  decoded = jwt.decode(IDjwt, public_key, algorithms=['RS256'])
  print(decoded)
  return(decoded)
