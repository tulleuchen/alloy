import os, sys, json
# this isn't working probably
if len(sys.argv) != 2:
  print("invalid number of arguments")
  print("usage")
  print("python3 ./context-to-env.py <contextJsonString>")
  print("e.g. python3 ./context-to-env.py '{\"NAME1\": \"VALUE1\",\"NAME2\": \"VALUE2\"}'")
  sys.exit(1)

if sys.argv[1] is not None:
  contextJson = sys.argv[1]
else:
  print("echo \"contextJson parameter is missing\"")
  sys.exit(1)

isTerraform = os.getenv('IS_TERRAFORM')

env_file = os.getenv('GITHUB_ENV')

try:
  jsonObj = json.loads(contextJson)
except ValueError as e:
  print("echo \"contextJson is not valid json string\"")
  sys.exit(0)

if jsonObj is not None:
  for contextItem in jsonObj:
    if contextItem == "ENV_JSON":
      continue
    print(contextItem + "=" + jsonObj[contextItem])
    envVarName=contextItem
    envVarValue=jsonObj[contextItem]

    if "GITHUB_ENV" in os.environ:
      if isTerraform == "true":
        print(f"export TF_VAR_{envVarName}={envVarValue};")
        print(f"echo \"TF_VAR_{envVarName}={envVarValue}\" >> $GITHUB_ENV")
      else:
        print(f"export {envVarName}={envVarValue};")
        print(f"echo \"{envVarName}={envVarValue}\" >> $GITHUB_ENV")
    else:
      if isTerraform == "true":
        print(f"export TF_VAR_{envVarName}={envVarValue}")
      else:
        print(f"export {envVarName}={envVarValue}")
