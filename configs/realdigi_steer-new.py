from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *
algList = []
evtsvc = EventDataSvc()


CONSTANTS = {
}

parseConstants(CONSTANTS)

read = LcioEvent()
read.OutputLevel = INFO
read.Files = ["input.slcio"]
algList.append(read)

DD4hep = MarlinProcessorWrapper("DD4hep")
DD4hep.OutputLevel = INFO
DD4hep.ProcessorType = "InitializeDD4hep"
DD4hep.Parameters = {
                     "DD4hepXMLFile": ["/path/to/compact/geometry/file.xml"],
                     "EncodingStringParameterName": ["GlobalTrackerReadoutID"]
                     }

Config = MarlinProcessorWrapper("Config")
Config.OutputLevel = INFO
Config.ProcessorType = "CLICRecoConfig"
Config.Parameters = {
                     "Overlay": ["False"],
                     "OverlayChoices": ["False", "None", "Test", "Trimmed", "Full"],
                     "VertexUnconstrained": ["OFF"],
                     "VertexUnconstrainedChoices": ["ON", "OFF"]
                     }

AIDA = MarlinProcessorWrapper("AIDA")
AIDA.OutputLevel = INFO
AIDA.ProcessorType = "AIDAProcessor"
AIDA.Parameters = {
                   "Compress": ["1"],
                   "FileName": ["output_digi"],
                   "FileType": ["root"]
                   }

EventNumber = MarlinProcessorWrapper("EventNumber")
EventNumber.OutputLevel = INFO
EventNumber.ProcessorType = "Statusmonitor"
EventNumber.Parameters = {
                          "HowOften": ["1"]
                          }

LCIOWriter_all = MarlinProcessorWrapper("LCIOWriter_all")
LCIOWriter_all.OutputLevel = INFO
LCIOWriter_all.ProcessorType = "LCIOOutputProcessor"
LCIOWriter_all.Parameters = {
                             "DropCollectionNames": [],
                             "DropCollectionTypes": [],
                             "FullSubsetCollections": [],
                             "KeepCollectionNames": [],
                             "LCIOOutputFile": ["output_digi.slcio"],
                             "LCIOWriteMode": ["WRITE_NEW"]
                             }

LCIOWriter_light = MarlinProcessorWrapper("LCIOWriter_light")
LCIOWriter_light.OutputLevel = INFO
LCIOWriter_light.ProcessorType = "LCIOOutputProcessor"
LCIOWriter_light.Parameters = {
                               "DropCollectionNames": ["MCParticle", "MCPhysicsParticle"],
                               "DropCollectionTypes": ["SimTrackerHit", "SimCalorimeterHit", "LCRelation"],
                               "FullSubsetCollections": [],
                               "KeepCollectionNames": [],
                               "LCIOOutputFile": ["output_digi_light.slcio"],
                               "LCIOWriteMode": ["WRITE_NEW"]
                               }

VXDBarrelDigitiser = MarlinProcessorWrapper("VXDBarrelDigitiser")
VXDBarrelDigitiser.OutputLevel = INFO
VXDBarrelDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDBarrelDigitiser.Parameters = {
                                 "CorrectTimesForPropagation": ["true"],
                                 "IsStrip": ["false"],
                                 "ResolutionT": ["0.03"],
                                 "ResolutionU": ["0.005"],
                                 "ResolutionV": ["0.005"],
                                 "SimTrackHitCollectionName": ["VertexBarrelCollection"],
                                 "SimTrkHitRelCollection": ["VXDBarrelHitsRelations"],
                                 "SubDetectorName": ["Vertex"],
                                 "TimeWindowMax": ["0.15"],
                                 "TimeWindowMin": ["-0.09"],
                                 "TrackerHitCollectionName": ["VXDBarrelHits"],
                                 "UseTimeWindow": ["true"]
                                 }

VXDEndcapDigitiser = MarlinProcessorWrapper("VXDEndcapDigitiser")
VXDEndcapDigitiser.OutputLevel = INFO
VXDEndcapDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDEndcapDigitiser.Parameters = {
                                 "CorrectTimesForPropagation": ["true"],
                                 "IsStrip": ["false"],
                                 "ResolutionT": ["0.03"],
                                 "ResolutionU": ["0.005"],
                                 "ResolutionV": ["0.005"],
                                 "SimTrackHitCollectionName": ["VertexEndcapCollection"],
                                 "SimTrkHitRelCollection": ["VXDEndcapHitsRelations"],
                                 "SubDetectorName": ["Vertex"],
                                 "TimeWindowMax": ["0.15"],
                                 "TimeWindowMin": ["-0.09"],
                                 "TrackerHitCollectionName": ["VXDEndcapHits"],
                                 "UseTimeWindow": ["true"]
                                 }

ITBarrelDigitiser = MarlinProcessorWrapper("ITBarrelDigitiser")
ITBarrelDigitiser.OutputLevel = INFO
ITBarrelDigitiser.ProcessorType = "DDPlanarDigiProcessor"
ITBarrelDigitiser.Parameters = {
                                "CorrectTimesForPropagation": ["true"],
                                "IsStrip": ["false"],
                                "ResolutionT": ["0.06"],
                                "ResolutionU": ["0.007"],
                                "ResolutionV": ["0.09"],
                                "SimTrackHitCollectionName": ["InnerTrackerBarrelCollection"],
                                "SimTrkHitRelCollection": ["ITBarrelHitsRelations"],
                                "SubDetectorName": ["InnerTrackers"],
                                "TimeWindowMax": ["0.3"],
                                "TimeWindowMin": ["-0.18"],
                                "TrackerHitCollectionName": ["ITBarrelHits"],
                                "UseTimeWindow": ["true"]
                                }

ITEndcapDigitiser = MarlinProcessorWrapper("ITEndcapDigitiser")
ITEndcapDigitiser.OutputLevel = INFO
ITEndcapDigitiser.ProcessorType = "DDPlanarDigiProcessor"
ITEndcapDigitiser.Parameters = {
                                "CorrectTimesForPropagation": ["true"],
                                "IsStrip": ["false"],
                                "ResolutionT": ["0.06"],
                                "ResolutionU": ["0.007"],
                                "ResolutionV": ["0.09"],
                                "SimTrackHitCollectionName": ["InnerTrackerEndcapCollection"],
                                "SimTrkHitRelCollection": ["ITEndcapHitsRelations"],
                                "SubDetectorName": ["InnerTrackers"],
                                "TimeWindowMax": ["0.3"],
                                "TimeWindowMin": ["-0.18"],
                                "TrackerHitCollectionName": ["ITEndcapHits"],
                                "UseTimeWindow": ["true"]
                                }

OTBarrelDigitiser = MarlinProcessorWrapper("OTBarrelDigitiser")
OTBarrelDigitiser.OutputLevel = INFO
OTBarrelDigitiser.ProcessorType = "DDPlanarDigiProcessor"
OTBarrelDigitiser.Parameters = {
                                "CorrectTimesForPropagation": ["true"],
                                "IsStrip": ["false"],
                                "ResolutionT": ["0.06"],
                                "ResolutionU": ["0.007"],
                                "ResolutionV": ["0.09"],
                                "SimTrackHitCollectionName": ["OuterTrackerBarrelCollection"],
                                "SimTrkHitRelCollection": ["OTBarrelHitsRelations"],
                                "SubDetectorName": ["OuterTrackers"],
                                "TimeWindowMax": ["0.3"],
                                "TimeWindowMin": ["-0.18"],
                                "TrackerHitCollectionName": ["OTBarrelHits"],
                                "UseTimeWindow": ["true"]
                                }

OTEndcapDigitiser = MarlinProcessorWrapper("OTEndcapDigitiser")
OTEndcapDigitiser.OutputLevel = INFO
OTEndcapDigitiser.ProcessorType = "DDPlanarDigiProcessor"
OTEndcapDigitiser.Parameters = {
                                "CorrectTimesForPropagation": ["true"],
                                "IsStrip": ["false"],
                                "ResolutionT": ["0.06"],
                                "ResolutionU": ["0.007"],
                                "ResolutionV": ["0.09"],
                                "SimTrackHitCollectionName": ["OuterTrackerEndcapCollection"],
                                "SimTrkHitRelCollection": ["OTEndcapHitsRelations"],
                                "SubDetectorName": ["OuterTrackers"],
                                "TimeWindowMax": ["0.3"],
                                "TimeWindowMin": ["-0.18"],
                                "TrackerHitCollectionName": ["OTEndcapHits"],
                                "UseTimeWindow": ["true"]
                                }

VXDBarrelRealisticDigi = MarlinProcessorWrapper("VXDBarrelRealisticDigi")
VXDBarrelRealisticDigi.OutputLevel = INFO
VXDBarrelRealisticDigi.ProcessorType = "MuonCVXDDigitiser"
VXDBarrelRealisticDigi.Parameters = {
                                     "ChargeDigitizeBinning": ["1"],
                                     "ChargeDigitizeNumBits": ["4"],
                                     "ChargeMaximum": ["15000."],
                                     "CollectionName": ["VertexBarrelCollection"],
                                     "CutOnDeltaRays": ["0.030"],
                                     "Diffusion": ["0.07"],
                                     "DigitizeCharge": ["1"],
                                     "DigitizeTime": ["0"],
                                     "ElectronicEffects": ["1"],
                                     "ElectronicNoise": ["80"],
                                     "ElectronsPerKeV": ["270.3"],
                                     "EnergyLoss": ["280.0"],
                                     "MaxEnergyDelta": ["100.0"],
                                     "MaxTrackLength": ["10.0"],
                                     "OutputCollectionName": ["VBTrackerHits"],
                                     "PixelSizeX": ["0.025"],
                                     "PixelSizeY": ["0.025"],
                                     "PoissonSmearing": ["1"],
                                     "RelationColName": ["VBTrackerHitsRelations"],
                                     "SegmentLength": ["0.005"],
                                     "StoreFiredPixels": ["1"],
                                     "SubDetectorName": ["VertexBarrel"],
                                     "TanLorentz": ["0.8"],
                                     "TanLorentzY": ["0.0"],
                                     "Threshold": ["500"],
                                     "ThresholdSmearSigma": ["25"],
                                     "TimeDigitizeBinning": ["0"],
                                     "TimeDigitizeNumBits": ["10"],
                                     "TimeMaximum": ["15.0"],
                                     "TimeSmearingSigma": ["0.03"]
                                     }

VXDEndcapRealisticDigi = MarlinProcessorWrapper("VXDEndcapRealisticDigi")
VXDEndcapRealisticDigi.OutputLevel = INFO
VXDEndcapRealisticDigi.ProcessorType = "MuonCVXDDigitiser"
VXDEndcapRealisticDigi.Parameters = {
                                     "ChargeDigitizeBinning": ["1"],
                                     "ChargeDigitizeNumBits": ["4"],
                                     "ChargeMaximum": ["15000."],
                                     "CollectionName": ["VertexEndcapCollection"],
                                     "CutOnDeltaRays": ["0.030"],
                                     "Diffusion": ["0.07"],
                                     "DigitizeCharge": ["1"],
                                     "DigitizeTime": ["0"],
                                     "ElectronicEffects": ["1"],
                                     "ElectronicNoise": ["80"],
                                     "ElectronsPerKeV": ["270.3"],
                                     "EnergyLoss": ["280.0"],
                                     "MaxEnergyDelta": ["100.0"],
                                     "MaxTrackLength": ["10.0"],
                                     "OutputCollectionName": ["VETrackerHits"],
                                     "PixelSizeX": ["0.025"],
                                     "PixelSizeY": ["0.025"],
                                     "PoissonSmearing": ["1"],
                                     "RelationColName": ["VETrackerHitsRelations"],
                                     "SegmentLength": ["0.005"],
                                     "StoreFiredPixels": ["1"],
                                     "SubDetectorName": ["VertexEndcap"],
                                     "TanLorentz": ["0.0"],
                                     "TanLorentzY": ["0.0"],
                                     "Threshold": ["500"],
                                     "ThresholdSmearSigma": ["25"],
                                     "TimeDigitizeBinning": ["0"],
                                     "TimeDigitizeNumBits": ["10"],
                                     "TimeMaximum": ["15.0"],
                                     "TimeSmearingSigma": ["0.03"]
                                     }

InnerPlanarRealisticDigi = MarlinProcessorWrapper("InnerPlanarRealisticDigi")
InnerPlanarRealisticDigi.OutputLevel = INFO
InnerPlanarRealisticDigi.ProcessorType = "MuonCVXDDigitiser"
InnerPlanarRealisticDigi.Parameters = {
                                       "ChargeDigitizeBinning": ["1"],
                                       "ChargeDigitizeNumBits": ["4"],
                                       "ChargeMaximum": ["60000."],
                                       "CollectionName": ["InnerTrackerBarrelCollection"],
                                       "CutOnDeltaRays": ["0.030"],
                                       "Diffusion": ["0.07"],
                                       "DigitizeCharge": ["1"],
                                       "DigitizeTime": ["0"],
                                       "ElectronicEffects": ["1"],
                                       "ElectronicNoise": ["80"],
                                       "ElectronsPerKeV": ["270.3"],
                                       "EnergyLoss": ["280.0"],
                                       "MaxEnergyDelta": ["100.0"],
                                       "MaxTrackLength": ["10.0"],
                                       "OutputCollectionName": ["IBTrackerHits"],
                                       "PixelSizeX": ["0.050"],
                                       "PixelSizeY": ["1.0"],
                                       "PoissonSmearing": ["1"],
                                       "RelationColName": ["IBTrackerHitsRelations"],
                                       "SegmentLength": ["0.005"],
                                       "StoreFiredPixels": ["1"],
                                       "SubDetectorName": ["InnerTrackerBarrel"],
                                       "TanLorentz": ["0.8"],
                                       "TanLorentzY": ["0.0"],
                                       "Threshold": ["1000."],
                                       "ThresholdSmearSigma": ["25"],
                                       "TimeDigitizeBinning": ["0"],
                                       "TimeDigitizeNumBits": ["10"],
                                       "TimeMaximum": ["15.0"],
                                       "TimeSmearingSigma": ["0.060"]
                                       }

InnerEndcapRealisticDigi = MarlinProcessorWrapper("InnerEndcapRealisticDigi")
InnerEndcapRealisticDigi.OutputLevel = INFO
InnerEndcapRealisticDigi.ProcessorType = "MuonCVXDDigitiser"
InnerEndcapRealisticDigi.Parameters = {
                                       "ChargeDigitizeBinning": ["1"],
                                       "ChargeDigitizeNumBits": ["4"],
                                       "ChargeMaximum": ["60000."],
                                       "CollectionName": ["InnerTrackerEndcapCollection"],
                                       "CutOnDeltaRays": ["0.030"],
                                       "Diffusion": ["0.07"],
                                       "DigitizeCharge": ["1"],
                                       "DigitizeTime": ["0"],
                                       "ElectronicEffects": ["1"],
                                       "ElectronicNoise": ["80"],
                                       "ElectronsPerKeV": ["270.3"],
                                       "EnergyLoss": ["280.0"],
                                       "MaxEnergyDelta": ["100.0"],
                                       "MaxTrackLength": ["10.0"],
                                       "OutputCollectionName": ["IETrackerHits"],
                                       "PixelSizeX": ["0.050"],
                                       "PixelSizeY": ["1.0"],
                                       "PoissonSmearing": ["1"],
                                       "RelationColName": ["IETrackerHitsRelations"],
                                       "SegmentLength": ["0.005"],
                                       "StoreFiredPixels": ["1"],
                                       "SubDetectorName": ["InnerTrackerEndcap"],
                                       "TanLorentz": ["0.0"],
                                       "TanLorentzY": ["0.0"],
                                       "Threshold": ["1000."],
                                       "ThresholdSmearSigma": ["25"],
                                       "TimeDigitizeBinning": ["0"],
                                       "TimeDigitizeNumBits": ["10"],
                                       "TimeMaximum": ["15.0"],
                                       "TimeSmearingSigma": ["0.060"]
                                       }

OuterPlanarRealisticDigi = MarlinProcessorWrapper("OuterPlanarRealisticDigi")
OuterPlanarRealisticDigi.OutputLevel = INFO
OuterPlanarRealisticDigi.ProcessorType = "MuonCVXDDigitiser"
OuterPlanarRealisticDigi.Parameters = {
                                       "ChargeDigitizeBinning": ["1"],
                                       "ChargeDigitizeNumBits": ["4"],
                                       "ChargeMaximum": ["60000."],
                                       "CollectionName": ["OuterTrackerBarrelCollection"],
                                       "CutOnDeltaRays": ["0.030"],
                                       "Diffusion": ["0.07"],
                                       "DigitizeCharge": ["1"],
                                       "DigitizeTime": ["0"],
                                       "ElectronicEffects": ["1"],
                                       "ElectronicNoise": ["80"],
                                       "ElectronsPerKeV": ["270.3"],
                                       "EnergyLoss": ["280.0"],
                                       "MaxEnergyDelta": ["100.0"],
                                       "MaxTrackLength": ["10.0"],
                                       "OutputCollectionName": ["OBTrackerHits"],
                                       "PixelSizeX": ["0.050"],
                                       "PixelSizeY": ["10.0"],
                                       "PoissonSmearing": ["1"],
                                       "RelationColName": ["OBTrackerHitsRelations"],
                                       "SegmentLength": ["0.005"],
                                       "StoreFiredPixels": ["1"],
                                       "SubDetectorName": ["OuterTrackerBarrel"],
                                       "TanLorentz": ["0.8"],
                                       "TanLorentzY": ["0.0"],
                                       "Threshold": ["1000."],
                                       "ThresholdSmearSigma": ["25"],
                                       "TimeDigitizeBinning": ["0"],
                                       "TimeDigitizeNumBits": ["10"],
                                       "TimeMaximum": ["15.0"],
                                       "TimeSmearingSigma": ["0.060"]
                                       }

OuterEndcapRealisticDigi = MarlinProcessorWrapper("OuterEndcapRealisticDigi")
OuterEndcapRealisticDigi.OutputLevel = INFO
OuterEndcapRealisticDigi.ProcessorType = "MuonCVXDDigitiser"
OuterEndcapRealisticDigi.Parameters = {
                                       "ChargeDigitizeBinning": ["1"],
                                       "ChargeDigitizeNumBits": ["4"],
                                       "ChargeMaximum": ["60000."],
                                       "CollectionName": ["OuterTrackerEndcapCollection"],
                                       "CutOnDeltaRays": ["0.030"],
                                       "Diffusion": ["0.07"],
                                       "DigitizeCharge": ["1"],
                                       "DigitizeTime": ["0"],
                                       "ElectronicEffects": ["1"],
                                       "ElectronicNoise": ["80"],
                                       "ElectronsPerKeV": ["270.3"],
                                       "EnergyLoss": ["280.0"],
                                       "MaxEnergyDelta": ["100.0"],
                                       "MaxTrackLength": ["10.0"],
                                       "OutputCollectionName": ["OETrackerHits"],
                                       "PixelSizeX": ["0.050"],
                                       "PixelSizeY": ["10.0"],
                                       "PoissonSmearing": ["1"],
                                       "RelationColName": ["OETrackerHitsRelations"],
                                       "SegmentLength": ["0.005"],
                                       "StoreFiredPixels": ["1"],
                                       "SubDetectorName": ["OuterTrackerEndcap"],
                                       "TanLorentz": ["0.0"],
                                       "TanLorentzY": ["0.0"],
                                       "Threshold": ["1000."],
                                       "ThresholdSmearSigma": ["25"],
                                       "TimeDigitizeBinning": ["0"],
                                       "TimeDigitizeNumBits": ["10"],
                                       "TimeMaximum": ["15.0"],
                                       "TimeSmearingSigma": ["0.060"]
                                       }

algList.append(AIDA)
algList.append(EventNumber)
algList.append(Config)
algList.append(DD4hep)
algList.append(VXDBarrelRealisticDigi)
algList.append(VXDEndcapRealisticDigi)
algList.append(InnerPlanarRealisticDigi)
algList.append(InnerEndcapRealisticDigi)
algList.append(OuterPlanarRealisticDigi)
algList.append(OTEndcapDigitiser)

from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc],
                OutputLevel=INFO
              )
