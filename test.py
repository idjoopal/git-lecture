# Copyright (c) 2023, Zikang Zhou. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from argparse import ArgumentParser

import pytorch_lightning as pl
from torch_geometric.loader import DataLoader
from transforms import TargetBuilder

from datasets import ArgoverseV2Dataset
from predictors import QCNet

from lightning_fabric.utilities.cloud_io import _load as pl_load
from lightning_fabric.utilities.cloud_io import _atomic_save as pl_save
import os


if __name__ == '__main__':
    pl.seed_everything(2023, workers=True)

    parser = ArgumentParser()
    parser.add_argument('--model', type=str, required=True)
    parser.add_argument('--root', type=str, required=True)
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--num_workers', type=int, default=8)
    parser.add_argument('--pin_memory', type=bool, default=True)
    parser.add_argument('--persistent_workers', type=bool, default=True)
    parser.add_argument('--accelerator', type=str, default='auto')
    parser.add_argument('--devices', type=int, default=1)
    parser.add_argument('--ckpt_path', type=str, required=True)
    args = parser.parse_args()

    # model = {
    #     'QCNet': QCNet,
    # }[args.model].load_from_checkpoint(checkpoint_path=args.ckpt_path)
    # model.num_historical_steps = 3
    # test_dataset = {
    #     'argoverse_v2': ArgoverseV2Dataset,
    # }[model.dataset](root=args.root, split='test')
    # dataloader = DataLoader(test_dataset, batch_size=args.batch_size, shuffle=False, num_workers=args.num_workers,
    #                         pin_memory=args.pin_memory, persistent_workers=args.persistent_workers)
    # trainer = pl.Trainer(accelerator=args.accelerator, devices=args.devices, strategy='ddp')
    # trainer.test(model, dataloader)

    model_output_dir = "/home/bjkim/workspace/storage/tmp"

    if not os.path.exists(model_output_dir):
        os.mkdir(model_output_dir)
    
    for idx in range(3, 110):
        # model_tmp = pl_load(args.ckpt_path)
        # model_tmp['hyper_parameters']['num_historical_steps'] = idx
        tmp_ckpt_path = f'{model_output_dir}/QCNet_AV2_{idx}.ckpt'
        # pl_save(model_tmp, tmp_ckpt_path)
        model = {
            'QCNet': QCNet,
        }[args.model].load_from_checkpoint(checkpoint_path=tmp_ckpt_path)
        print(f'load historical_step: {model.num_historical_steps}')

        test_dataset = {
            'argoverse_v2': ArgoverseV2Dataset,
        }[model.dataset](root=args.root, split='val')
        dataloader = DataLoader(test_dataset, batch_size=args.batch_size, shuffle=False, num_workers=args.num_workers,
                                pin_memory=args.pin_memory, persistent_workers=args.persistent_workers)
        trainer = pl.Trainer(accelerator=args.accelerator, devices=args.devices, strategy='ddp')
        trainer.test(model, dataloader)
