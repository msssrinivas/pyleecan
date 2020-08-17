# -*- coding: utf-8 -*-
"""File generated by generate_code() - pyleecan-public/pyleecan/Generator/run_generate_classes.py
WARNING! All changes made in this file will be lost!
"""

from ..Classes.import_all import *

load_switch = {
    "Arc": Arc,
    "Arc1": Arc1,
    "Arc2": Arc2,
    "Arc3": Arc3,
    "Bore": Bore,
    "BoreFlower": BoreFlower,
    "CellMat": CellMat,
    "Circle": Circle,
    "CondType11": CondType11,
    "CondType12": CondType12,
    "CondType21": CondType21,
    "CondType22": CondType22,
    "Conductor": Conductor,
    "DataKeeper": DataKeeper,
    "Drive": Drive,
    "DriveWave": DriveWave,
    "EEC": EEC,
    "EEC_PMSM": EEC_PMSM,
    "Electrical": Electrical,
    "FluxLink": FluxLink,
    "FluxLinkFEMM": FluxLinkFEMM,
    "Force": Force,
    "ForceMT": ForceMT,
    "Frame": Frame,
    "GUIOption": GUIOption,
    "Hole": Hole,
    "HoleM50": HoleM50,
    "HoleM51": HoleM51,
    "HoleM52": HoleM52,
    "HoleM53": HoleM53,
    "HoleM54": HoleM54,
    "HoleM57": HoleM57,
    "HoleM58": HoleM58,
    "HoleMag": HoleMag,
    "Import": Import,
    "ImportData": ImportData,
    "ImportGenMatrixSin": ImportGenMatrixSin,
    "ImportGenToothSaw": ImportGenToothSaw,
    "ImportGenVectLin": ImportGenVectLin,
    "ImportGenVectSin": ImportGenVectSin,
    "ImportMatlab": ImportMatlab,
    "ImportMatrix": ImportMatrix,
    "ImportMatrixVal": ImportMatrixVal,
    "ImportMatrixXls": ImportMatrixXls,
    "ImportVectorField": ImportVectorField,
    "IndMag": IndMag,
    "IndMagFEMM": IndMagFEMM,
    "Input": Input,
    "InputCurrent": InputCurrent,
    "InputFlux": InputFlux,
    "InputForce": InputForce,
    "LamHole": LamHole,
    "LamSlot": LamSlot,
    "LamSlotMag": LamSlotMag,
    "LamSlotMulti": LamSlotMulti,
    "LamSlotWind": LamSlotWind,
    "LamSquirrelCage": LamSquirrelCage,
    "Lamination": Lamination,
    "Line": Line,
    "Machine": Machine,
    "MachineAsync": MachineAsync,
    "MachineDFIM": MachineDFIM,
    "MachineIPMSM": MachineIPMSM,
    "MachineSCIM": MachineSCIM,
    "MachineSIPMSM": MachineSIPMSM,
    "MachineSRM": MachineSRM,
    "MachineSyRM": MachineSyRM,
    "MachineSync": MachineSync,
    "MachineUD": MachineUD,
    "MachineWRSM": MachineWRSM,
    "MagFEMM": MagFEMM,
    "Magnet": Magnet,
    "MagnetFlat": MagnetFlat,
    "MagnetPolar": MagnetPolar,
    "MagnetType10": MagnetType10,
    "MagnetType11": MagnetType11,
    "MagnetType12": MagnetType12,
    "MagnetType13": MagnetType13,
    "MagnetType14": MagnetType14,
    "Magnetics": Magnetics,
    "MatEconomical": MatEconomical,
    "MatElectrical": MatElectrical,
    "MatHT": MatHT,
    "MatMagnetics": MatMagnetics,
    "MatStructural": MatStructural,
    "Material": Material,
    "Mesh": Mesh,
    "MeshMat": MeshMat,
    "MeshSolution": MeshSolution,
    "MeshVTK": MeshVTK,
    "Mode": Mode,
    "Notch": Notch,
    "NotchEvenDist": NotchEvenDist,
    "OptiConstraint": OptiConstraint,
    "OptiDesignVar": OptiDesignVar,
    "OptiGenAlg": OptiGenAlg,
    "OptiGenAlgNsga2Deap": OptiGenAlgNsga2Deap,
    "OptiObjFunc": OptiObjFunc,
    "OptiProblem": OptiProblem,
    "OptiSolver": OptiSolver,
    "OutElec": OutElec,
    "OutForce": OutForce,
    "OutGeo": OutGeo,
    "OutGeoLam": OutGeoLam,
    "OutMag": OutMag,
    "OutPost": OutPost,
    "OutStruct": OutStruct,
    "Output": Output,
    "OutputMulti": OutputMulti,
    "OutputMultiOpti": OutputMultiOpti,
    "ParamExplorer": ParamExplorer,
    "ParamExplorerSet": ParamExplorerSet,
    "PointMat": PointMat,
    "PolarArc": PolarArc,
    "Segment": Segment,
    "Shaft": Shaft,
    "Simu1": Simu1,
    "Simulation": Simulation,
    "Slot": Slot,
    "Slot19": Slot19,
    "SlotCirc": SlotCirc,
    "SlotMFlat": SlotMFlat,
    "SlotMPolar": SlotMPolar,
    "SlotMag": SlotMag,
    "SlotUD": SlotUD,
    "SlotW10": SlotW10,
    "SlotW11": SlotW11,
    "SlotW12": SlotW12,
    "SlotW13": SlotW13,
    "SlotW14": SlotW14,
    "SlotW15": SlotW15,
    "SlotW16": SlotW16,
    "SlotW21": SlotW21,
    "SlotW22": SlotW22,
    "SlotW23": SlotW23,
    "SlotW24": SlotW24,
    "SlotW25": SlotW25,
    "SlotW26": SlotW26,
    "SlotW27": SlotW27,
    "SlotW28": SlotW28,
    "SlotW29": SlotW29,
    "SlotW60": SlotW60,
    "SlotW61": SlotW61,
    "SlotWind": SlotWind,
    "Solution": Solution,
    "SolutionData": SolutionData,
    "SolutionMat": SolutionMat,
    "SolutionVector": SolutionVector,
    "Structural": Structural,
    "SurfLine": SurfLine,
    "SurfRing": SurfRing,
    "Surface": Surface,
    "Trapeze": Trapeze,
    "Unit": Unit,
    "VarLoad": VarLoad,
    "VarLoadCurrent": VarLoadCurrent,
    "VarParam": VarParam,
    "VarSimu": VarSimu,
    "VentilationCirc": VentilationCirc,
    "VentilationPolar": VentilationPolar,
    "VentilationTrap": VentilationTrap,
    "Winding": Winding,
    "WindingCW1L": WindingCW1L,
    "WindingCW2LR": WindingCW2LR,
    "WindingCW2LT": WindingCW2LT,
    "WindingDW1L": WindingDW1L,
    "WindingDW2L": WindingDW2L,
    "WindingSC": WindingSC,
    "WindingUD": WindingUD,
    "XOutput": XOutput,
}
