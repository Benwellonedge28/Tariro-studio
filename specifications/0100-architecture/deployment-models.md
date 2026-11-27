# Deployment modes

**Contract version** 1.0. Master design §71.

Standalone is the initial reference mode. Offline denies all external egress. Air-gapped additionally disables discovery and external integration bindings. Online and hybrid enable only explicitly configured endpoints. Headless shares the same supervised runtime as CLI; remote control requires authenticated secure transport.

## Implementation and acceptance

Advertise chosen deployment mode and available features on startup. Embedded, enterprise, research and distributed modes use scoped adapters and independent acceptance gates. A mode change revalidates active grants before new effects.
