
# This lists the CDDL types that are autolinked in the main Open Screen Protocol
# specification.  Only these types will be wrapped in <dfn> tags and treated as
# definitions.
LINKED_TYPES = frozenset([
  'agent-info',
  'agent-info-event',
  'agent-info-request',
  'agent-info-response',
  'agent-status-request',
  'agent-status-response',
  'audio-frame',
  'auth-capabilities',
  'auth-initiation-token',
  'auth-spake2-confirmation',
  'auth-spake2-message',
  'auth-spake2-need-psk',
  'auth-status',  
  'data-frame',
  'media-time',
  'presentation-change-event',
  'presentation-connection-close-event',
  'presentation-connection-message',
  'presentation-connection-open-request',
  'presentation-connection-open-response',
  'presentation-start-request',
  'presentation-start-response',
  'presentation-termination-event',
  'presentation-termination-request',
  'presentation-termination-response',
  'presentation-url-availability-event',
  'presentation-url-availability-request',
  'presentation-url-availability-response',
  'remote-playback-availability-event',
  'remote-playback-availability-request',
  'remote-playback-availability-response',
  'remote-playback-modify-request',
  'remote-playback-modify-response',
  'remote-playback-start-request',
  'remote-playback-start-response',
  'remote-playback-state-event',
  'remote-playback-termination-event',
  'remote-playback-termination-request',
  'remote-playback-termination-response',
  'streaming-capabilities-request',
  'streaming-capabilities-response',
  'text-track-cue',
  'video-frame',
])

