## Charts

### The Chart file structure

The directory name is the name of the chart (without versioning information).
Helm reserves use of the charts/ , crds/ , and templates/ directories.
- Chart.yaml
- LICENSE
- README.md
- values.yaml
- values.schema.json
- charts
- crds
- templates
- templates/NOTES.txt

### The Chart.yaml file

```yaml
apiVersion: The chart API version (required)
name: The name of the chart (required)
version: A SemVer 2 version (required)
kubeVersion: A SemVer range of compatible Kubernetes versions (optional)
description: A single-sentence description of this project (optional)
type: The type of the chart (optional)
keywords:
  - A list of keywords about this project (optional)
home: The URL of this projects home page (optional)
sources:
  - A list of URLs to source code for this project (optinoal)
dependencies: # A list of the chart requirements (optional)
  - name: The name of the chart
    version: The version of the chart
    repository: The repository URL or alias
    condition: (optional) A yaml path that resolves to a boolean, used for enabling/disabling chart
    tags: # (optional)
      - Tags can be used to group charts for enabling/disabling together
    enabled: (optional) Enabled bool determines if chart should be loaded
    import-values: # (optional)
      - ImportValues holds the mapping of source values to parent key to be imported. Each item can be a string or pair of child/parent sublist items.
    alias: (optional) Alias to be used for the chart. Useful when you have to add the same chart multiple times
maintainers: # (optional)
  - name: The maintainers name
    email: The maintainers email
    url: A URL for the maintainer
icon: A URL to an SVG or PNG image to be used as an icon (optional)
appVersion: The version of the app that this contains (optional).
deprecated: Whether this chart is deprecated (optional, boolean)
annotations:
  example: A list of annotations keyed by name (optional).

```

### Charts and Versioning

For example, an nginx chart whose version field is set to version: 1.2.3 will be named nginx-1.2.3.tgz
The system assumes that the version number in the chart package name matches the version number in the Chart.yaml . Failure to meet this assumption will cause an error.

### Deprecating Charts

If the latest version of a chart in the repository is marked as deprecated, then the chart as a whole is considered to be deprecated. The workflow for deprecating charts:
1. Update chart's Chart.yaml to mark the chart as deprecated, bumping the version
2. Release the new chart version in the Chart Repository
3. Remove the chart from the source repository e.g. git

### Managing Dependencies with the dependencies field

```
dependencies:
  - name: apache
    version: 1.2.3
    repository: https://example.com/charts
  - name: mysql
    version: 3.2.1
    repository: https://another.example.com/charts
```

The repository field is the full URL to the chart repository. Note that you must also use `helm repo add` to add that repo locally. You might use the name of the repo instead of URL.

`$ helm repo add fantastic-charts https://fantastic-charts.storage.googleapis.com`

```
dependencies:
  - name: awesomeness
    version: 1.0.0
    repository: "@fantastic-charts"
```

`helm dependency update` will use your dependency file to download all the specified charts into the charts/ directory.
One can use `alias` field in cases where they need to access a chart with other name(s).

optionals fields `tags` and `condition` 

```
# parentchart/Chart.yaml

dependencies:
  - name: subchart1
    repository: http://localhost:10191
    version: 0.1.0
    condition: subchart1.enabled, global.subchart1.enabled
    tags:
      - front-end
      - subchart1
  - name: subchart2
    repository: http://localhost:10191
    version: 0.1.0
    condition: subchart2.enabled,global.subchart2.enabled
    tags:
      - back-end
      - subchart2
```

```
# parentchart/values.yaml

subchart1:
  enabled: true
tags:
  front-end: false
  back-end: true
```

Using the CLI with Tags and Conditions

`helm install --set tags.front-end=true --set subchart2.enabled=false`

Tags and Condition Resolution
- Conditions (when set in values) always override tags. The first condition path that exists wins and subsequent ones for that chart are ignored.
- Tags are evaluated as 'if any of the chart's tags are true then enable the chart'.
- Tags and conditions values must be set in the top parent's values.
- The tags: key in values must be a top level key. Globals and nested tags: tables are not currently supported.

Importing Child Values via dependencies

```
# parent's Chart.yaml file

dependencies:
  - name: subchart
    repository: http://localhost:10191
    version: 0.1.0
    import-values:
      - data

# child's values.yaml file

exports:
  data:
    myint: 99

# parent's values
myint: 99
```

Using the child-parent format

```
# parent's Chart.yaml file

dependencies:
  - name: subchart1
    repository: http://localhost:10191
    version: 0.1.0
    ...
    import-values:
      - child: default.data
        parent: myimports

# parent's values.yaml file

myimports:
  myint: 0
  mybool: false
  mystring: "helm rocks!"
# subchart1's values.yaml file

default:
  data:
    myint: 999
    mybool: true

# parent's final values

myimports:
  myint: 999
  mybool: true
  mystring: "helm rocks!"


```

TIP: To drop a dependency into your charts/ directory, use the `helm pull` command

### Templates and Values

Helm Chart templates are written in the Go template language. All template files are stored in a chart's templates/ folder.
Values for the templates are supplied two ways:
- Chart developers may supply a file called values.yaml. This file can contain default values.
- Chart users may supply a YAML file that contains values. This can be provided on the command line with `helm install`.

When a user supplies custom values, these values will override the values in the chart's values.yaml file.

Values are supplied via a values.yaml file or via the --set flag. They are accessible from the {{ .Values. }} object in a template.

The following values are pre-defined, are available to every template, and cannot be overridden.
- Release.Name
- Release.Namespace
- Release.Service
- Release.IsUpgrade : This is set to true if the current operation is an upgrade or rollback.
- Release.IsInstall : This is set to true if the current operation is an install.
- Chart : The contents of the Chart.yaml. Thus, the chart version is obtainable as Chart.Version
- Files : A map-like object containing all non-special files in the chart.
- Capabilities : A map-like object that contains information about the versions of Kubernetes ( {{ .Capabilities.KubeVersion }}) and the supported Kubernetes API versions.

Chart.yaml cannot be used to pass arbitrarily structured data into the template. The values file can be used for that.

A values file is formatted in YAML. The Helm install command allows a user to override values by supplying additional YAML values e.g.:

`$ helm install --generate-name --values=myvals.yaml wordpress`

#### Scope, Dependencies, and Values

Global Values: .Values.global.xxx
This is useful for things like setting metadata properties like labels.
If a subchart declares a global variable, that global will be passed downward, but not upward to the parent chart. Also, global variables of parent chart take precedence over the global variables from subcharts.

### Schema Files

Use to define a structure on their values. `values.schema.json` file. A schema is represented as a JSON Schema.
Validation occurs when any of the following commands are invoked:
helm install, helm upgrade, helm lint, helm template

### Custom Resource Definitions (CRDs)

CRDs are treated as a special kind of object. They are installed before the rest of the chart, and are subject to some limitations.
CRD YAML files should be placed in the crds/ directory inside of a chart.
CRD files cannot be templated. They must be plain YAML documents.
Helm will make sure that the CRD kind has been installed and is available from the Kubernetes API server before it proceeds installing the things in templates/

### Limitations of CRDs

CRDs are installed globally. Limitations:
- CRDs are never reinstalled. If Helm determines that the CRDs in the crds/ directory are already present (regardless of version). Helm will not attempt to install or upgrade.
- CRDs are never installed on upgrade or rollback. Helm will only create CRDs on installation operations.
- CRDs are never deleted. Helm will not delete CRDs.

Operators who want to upgrade or delete CRDs are encouraged to do this manually and with great care.


## Chart Hooks
